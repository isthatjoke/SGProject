from django.contrib import admin

# Register your models here.

from post.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'hub_category', 'published', 'user_id', 'created_at')
    list_display_links = ('name',)
    search_fields = ('hub_category', 'user_id', 'published', 'created_at')


admin.site.register(Post, PostAdmin)



