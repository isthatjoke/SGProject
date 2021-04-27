from django.contrib import admin

# Register your models here.

from post.models import Post, PostKarma, Tags


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'hub_category', 'status', 'user_id', 'created_at')
    list_display_links = ('name',)
    search_fields = ('hub_category', 'user_id', 'created_at', 'status')

class TagsAdmin(admin.ModelAdmin):
    list_display = ('name')

admin.site.register(Post, PostAdmin)
admin.site.register(PostKarma)
admin.site.register(Tags)


