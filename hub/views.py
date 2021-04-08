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

    content = {
        'head_menu_object_list': head_menu_object_list,
        'all_posts_object_list': all_posts,
    }

    return render(request, 'hub/index.html', context=content)


class HubCategoryPostListView(ListView):
    model = HubCategory
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'hub/hubcategory_list.html'

    def get_queryset(self):
        return Post.objects.filter(hub_category__category_id=self.kwargs.get('pk', '')).select_related()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HubCategoryPostListView, self).get_context_data(**kwargs)
        context['head_menu_object_list'] = get_hub_cats_dict()

        return context



