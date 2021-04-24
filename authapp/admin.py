from django.contrib import admin

# Register your models here.

from authapp.models import HubUser, HubUserProfile


class HubUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_superuser', 'is_staff', 'banned')


admin.site.register(HubUser, HubUserAdmin)
admin.site.register(HubUserProfile)
