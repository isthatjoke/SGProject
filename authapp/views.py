from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView, CreateView, UpdateView

# Create your views here.
from django_tables2 import SingleTableView
from notifications.signals import notify

from authapp.forms import HubUserLoginForm, HubUserRegisterForm, HubUserUpdateForm, HubUserProfileUpdateForm
from authapp.models import HubUser
from authapp.tables import UsersRatingTable
from backend.utils import LoginRequiredDispatchMixin


class HubUserLoginView(LoginView):
    form_class = HubUserLoginForm
    template_name = 'authapp/login.html'
    success_url = reverse_lazy('hub:main')
    redirect_field_name = 'next'


class HubUserRegisterView(CreateView):
    form_class = HubUserRegisterForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('authapp:login')


class HubUserUpdateView(UpdateView, SuccessMessageMixin, LoginRequiredDispatchMixin):
    model = HubUser
    template_name = 'authapp/update.html'
    form_class = HubUserUpdateForm
    success_url = reverse_lazy('authapp:update')
    success_message = 'профиль обновлен'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(HubUserUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            update_form = HubUserUpdateForm(self.request.POST, instance=self.object)
            profile_form = HubUserProfileUpdateForm(self.request.POST, instance=self.object.hubuserprofile)
        else:
            update_form = HubUserUpdateForm(instance=self.object)
            profile_form = HubUserProfileUpdateForm(instance=self.object.hubuserprofile)
        context['update_form'] = update_form
        context['profile_form'] = profile_form

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        hubuserprofile = context['profile_form']
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        with transaction.atomic():
            self.object = form.save()
            if hubuserprofile.is_valid():
                hubuserprofile.save()
        notify.send(self.object, recipient=self.object, verb='you reached level 10')
        return super(HubUserUpdateView, self).form_valid(form)


class HubUserLogoutView(LogoutView):
    template_name = 'authapp/success.html'
    next_page = '/'


class Success(TemplateView):
    template_name = 'authapp/success.html'


class UsersRatingListView(SingleTableView):
    model = HubUser
    table_class = UsersRatingTable
    template_name = 'authapp/users_rating.html'
    context_table_name = 'users'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersRatingListView, self).get_context_data(**kwargs)
        context['title'] = 'Рейтинг пользователей'
        return context

    def get_queryset(self):
        users = HubUser.objects.all().order_by('-rating')
        return users