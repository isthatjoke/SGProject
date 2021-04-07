from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView, CreateView, UpdateView

# Create your views here.
from authapp.forms import HubUserLoginForm, HubUserRegisterForm, HubUserUpdateForm, HubUserProfileUpdateForm
from authapp.models import HubUser


class HubUserLoginView(LoginView):
    form_class = HubUserLoginForm
    template_name = 'authapp/login.html'

    def get_success_url(self):

        return reverse('hub:main')


class HubUserRegisterView(CreateView):
    form_class = HubUserRegisterForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('authapp:success')


class HubUserUpdateView(UpdateView):
    model = HubUser
    template_name = 'authapp/update.html'
    form_class = HubUserUpdateForm
    success_url = reverse_lazy('authapp:success')

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

        with transaction.atomic():
            self.object = form.save()
            if hubuserprofile.is_valid():
                hubuserprofile.save()
        return super(HubUserUpdateView, self).form_valid(form)


class HubUserLogoutView(LogoutView):
    template_name = 'authapp/success.html'
    next_page = '/'


class Success(TemplateView):
    template_name = 'authapp/success.html'



