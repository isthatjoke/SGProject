from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import View, ContextMixin
from django.db.models import Count

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
    ordering = ('-updated_at',)

    def get_queryset(self):
        return Post.objects.filter(status=Post.STATUS_PUBLISHED).select_related()

    def get_queryset(self):
        return ordering(self.request)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Main, self).get_context_data(**kwargs)
        context['head_menu_object_list'] = get_hub_cats_dict()
        context['title'] = 'Hub'

        return context


class HubPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'hub/index.html'

    def get_queryset(self):

        return ordering(self.request, pk=self.kwargs.get('pk', ''))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HubPostListView, self).get_context_data(**kwargs)
        category = Hub.objects.get(pk=self.kwargs.get('pk', ''))
        context['head_menu_object_list'] = get_hub_cats_dict()
        context['title'] = category.name
        context['msg_type'] = self.request.GET.get('msg_type', '')
        context['days'] = self.request.GET.get('days', '')

        return context


class HubCategoryPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'hub/index.html'

    def get_queryset(self):
        return ordering(self.request, cat=self.kwargs.get('cat', ''))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HubCategoryPostListView, self).get_context_data(**kwargs)
        category = Hub.objects.get(pk=self.kwargs.get('pk', ''))
        hub_category = HubCategory.objects.get(pk=self.kwargs.get('cat', ''))
        context['head_menu_object_list'] = get_hub_cats_dict()
        context['title'] = category.name
        context['hub_category'] = hub_category.name
        context['msg_type'] = self.request.GET.get('msg_type', '')
        context['days'] = self.request.GET.get('days', '')

        return context


def ordering(request, pk=None, cat=None):

    days_count = int(request.GET.get('days', 20))
    now = datetime.now(pytz.timezone(settings.TIME_ZONE)) - timedelta(days=days_count)
    posts = Post.objects.filter(status=Post.STATUS_PUBLISHED).select_related().filter(updated_at__gte=now)

    if pk is not None:
        posts = posts.filter(hub_category__category_id=pk)

    if cat is not None:
        posts = posts.filter(hub_category=cat)

    if request.GET.get('msg_type') == '+date':
        posts = posts.order_by('-updated_at')

    elif request.GET.get('msg_type') == '-date':
        posts = posts.order_by('updated_at')

    elif request.GET.get('msg_type') == '+karma':
        posts = posts.annotate(num_karam=Count('post_id')).order_by('post_id')

    elif request.GET.get('msg_type') == '-karma':
        posts = posts.annotate(num_karam=Count('post_id')).order_by('-post_id')

    return posts





