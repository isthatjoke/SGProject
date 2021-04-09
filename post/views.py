from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView

from hub.models import get_hub_cats_dict
from post.models import Post


class PostDetailView(DetailView):
    template_name = 'post/post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['head_menu_object_list'] = get_hub_cats_dict()

        return context


