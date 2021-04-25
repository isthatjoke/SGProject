from django.contrib import admin

# Register your models here.

from hub.models import Hub, HubCategory, HubCategoryUsers

admin.site.register(Hub)
admin.site.register(HubCategory)
admin.site.register(HubCategoryUsers)


