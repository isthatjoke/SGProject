from django_tables2 import Table, Column, A

from post.models import Post


class PostsTable(Table):
    name = Column(linkify=('post:post', {'pk': A('pk')}))

    class Meta:
        model = Post
        fields = ("name", "hub_category", "karma_count", "created_at",
                  "updated_at",)


class ModeratorPostsTable(Table):
    name = Column(linkify=('post:post', {'pk': A('pk')}))

    class Meta:
        model = Post
        fields = ("name", "hub_category", "status", "user", "created_at",
                  "updated_at",)
