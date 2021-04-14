from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import View, ContextMixin

from hub.models import Hub, HubCategory, get_hub_cats_dict
from post.models import Post


class CustomDispatchMixin(View):

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BaseClassContextMixin(ContextMixin):
    title = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


def main(request):
    head_menu_object_list = get_hub_cats_dict()
    all_posts = Post.get_all_posts()
    title = 'Hub'

    content = {
        'head_menu_object_list': head_menu_object_list,
        'posts': all_posts,
        'title': title,
    }

    return render(request, 'hub/index.html', context=content)


class Main(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'hub/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Main, self).get_context_data(**kwargs)
        context['head_menu_object_list'] = get_hub_cats_dict()
        context['title'] = 'Hub'

        return context


class HubPostListView(ListView):
    model = HubCategory
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'hub/index.html'

    def get_queryset(self):
        return Post.objects.filter(hub_category__category_id=self.kwargs.get('pk', '')).\
            filter(published=True).select_related()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HubPostListView, self).get_context_data(**kwargs)
        category = Hub.objects.get(pk=self.kwargs.get('pk', ''))
        context['head_menu_object_list'] = get_hub_cats_dict()
        context['title'] = category.name

        return context


class HubCategoryPostListView(ListView):
    model = HubCategory
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'hub/index.html'

    def get_queryset(self):
        return Post.objects.filter(hub_category=self.kwargs.get('cat', '')).\
            filter(published=True).select_related()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HubCategoryPostListView, self).get_context_data(**kwargs)
        category = Hub.objects.get(pk=self.kwargs.get('pk', ''))
        context['head_menu_object_list'] = get_hub_cats_dict()
        context['title'] = category.name

        return context

