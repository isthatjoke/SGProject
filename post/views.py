from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, ListView, UpdateView


from hub.models import get_hub_cats_dict
from post.forms import PostEditForm
from post.models import Post


class PostDetailView(DetailView):
    template_name = 'post/post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['head_menu_object_list'] = get_hub_cats_dict()
        context['title'] = f'Пост - {self.object.name}'

        return context


class PostCreateView(CreateView):
    template_name = 'post/post_form.html'
    form_class = PostEditForm
    success_url = reverse_lazy('hub:main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['form']['user_id'].initial = self.request.user
        context['title'] = f'Создание поста'
        return context

    def get_success_url(self):
        return reverse('post:post', kwargs={'pk': self.object.pk})


class PostUserListView(ListView):
    model = Post
    template_name = 'hub/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostUserListView, self).get_context_data(**kwargs)
        context['title'] = f'Мои посты'
        return context


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post_form.html'
    form_class = PostEditForm
    success_url = reverse_lazy('hub:main')

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['title'] = f'Редактирование поста {self.object.name}'

        return context

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk', None))
        if post.published is True:
            return HttpResponseRedirect(reverse('post:post', kwargs={'pk': post.id}))

