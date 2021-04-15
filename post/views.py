from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, ListView, UpdateView

from authapp.models import HubUser
from hub.models import get_hub_cats_dict
from post.forms import PostEditForm
from post.models import Post, PostKarma


def perform_karma_update(post_id: int, user_id: int, karma: int):
    """
    Функция выполняющая несколько проверок, прежде чем поставить карму для поста.
    Сначала функция проверяет, чтобы юзер не оценивал свой собственный пост.
    Далее функция проверяет, чтобы юзер оценивал пост в первый раз (повторно оценивать пост нельзя).
    Если все проверки пройдены, то функция возвращает соответствующий ответ в формате JSON.

    :param post_id: идентификатор поста, с которым взаимодействуют
    :param user_id: идентификатор пользователя, который взаимодействует
    :param karma: оценка, может быть 1 или -1
    :return:
    """
    already_liked = PostKarma.objects.filter(Q(user_id=user_id) & Q(post_id=post_id))
    post = get_object_or_404(Post, id=post_id)
    user = get_object_or_404(HubUser, id=user_id)
    if user_id == post.user_id.id:
        resp = 'Нельзя оценивать свой собственный пост!'
        return JsonResponse({'result': resp})
    elif not already_liked:
        new_object = PostKarma.objects.create(post_id=post, user_id=user, karma=karma)
        new_object.save()
        post = Post.objects.filter(id=post_id).first().post_karma
        return JsonResponse({'result': str(post)})
    else:
        resp = 'Вы уже оценили этот пост!'
        return JsonResponse({'result': resp})


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


@login_required
def karma_update(request, pk, pk2):
    '''
    функция обработки ajax запроса на изменение кармы поста
    :param request:
    :param pk: id поста в таблице Post
    :param pk2: сигнал (если 1 - значит поставили лайк, если 0 - то поставили дизлайк)
    :return: возвращает карму прочитанную из БД в виде json
    '''

    if request.is_ajax():
        user_id = get_object_or_404(HubUser, id=request.user.id).id
        result = None
        if pk2 == 1:
            result = perform_karma_update(pk, user_id, 1)
        elif pk2 == 0:
            result = perform_karma_update(pk, user_id, -1)
        if result:
            return result
