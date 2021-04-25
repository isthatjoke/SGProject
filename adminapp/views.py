from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from authapp.models import HubUser
# Create your views here.


class HubUserListView(ListView):
    model = HubUser
    template_name = 'adminapp/users_list.html'
    context_object_name = 'users'
    paginate_by = 10

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, *args, **kwargs):
        return super(HubUserListView, self).dispatch(*args, **kwargs)





