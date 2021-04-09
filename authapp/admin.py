from django.contrib import admin

# Register your models here.

from authapp.models import HubUser, HubUserProfile

admin.site.register(HubUser)
admin.site.register(HubUserProfile)
