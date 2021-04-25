from django.contrib import admin

# Register your models here.

from post.models import Post, PostKarma


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'hub_category', 'status', 'user_id', 'created_at')
    list_display_links = ('name',)
    search_fields = ('hub_category', 'user_id', 'created_at', 'status')


admin.site.register(Post, PostAdmin)
admin.site.register(PostKarma)


