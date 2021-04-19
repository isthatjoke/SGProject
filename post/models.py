import json

from django.db import models
from django.shortcuts import redirect

from authapp.models import HubUser, HubUserProfile
from hub.models import HubCategory, Hub
from ckeditor.fields import RichTextField

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    STATUS_PUBLISHED = 'published'
    STATUS_UNPUBLISHED = 'unpublished'
    STATUS_ARCHIVE = 'archive'
    STATUS_TEMPLATE = 'template'

    STATUSES = (
        (STATUS_PUBLISHED, 'опубликован'),
        (STATUS_UNPUBLISHED, 'неопубликован'),
        (STATUS_ARCHIVE, 'в архиве'),
        (STATUS_TEMPLATE, 'шаблон')
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)

    name = models.CharField(max_length=200, verbose_name='название', )
    # short_desc = models.CharField(max_length=200, verbose_name='краткое описание', )
    # post_text = models.TextField(verbose_name='пост', blank=False, null=True)
    hub_category = models.ForeignKey(HubCategory, related_name='hub_category',
                                     verbose_name='подкатегория', on_delete=models.CASCADE, **NULLABLE)
    status = models.CharField(verbose_name='статус', choices=STATUSES, default=STATUS_UNPUBLISHED, max_length=11)
    # published = models.BooleanField(default=False, verbose_name='опубликовано', )
    user_id = models.ForeignKey(HubUser, related_name='user_id', verbose_name='пользователь', on_delete=models.CASCADE,
                                **NULLABLE)
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add=True, )
    updated_at = models.DateTimeField(verbose_name='время обновления', auto_now=True, )
    content = RichTextField()

    # Метод возвращает посты конкретного пользователя
    # pk - id пользователя
    @staticmethod
    def get_user_posts(pk):
        return Post.objects.filter(user=pk).order_by('-updated_at')

    def __str__(self):
        return f'{self.name} ({self.hub_category.name})'

    # Метод возвращает все посты всех пользователей и сортирует по дате
    @staticmethod
    def get_all_posts():
        return Post.objects.filter(status=Post.STATUS_PUBLISHED).order_by('-updated_at')

    # свойство класса для интерактивного подсчета кармы
    @property
    def post_karma(self):
        return self.post_id.count()
        # karma_objects = self.post_id.all()
        # karma = 0
        # for obj in karma_objects:
        #     karma += obj.karma
        # return karma


class PostKarma(models.Model):
    class Meta:
        verbose_name = 'карма поста'
        verbose_name_plural = 'Карма постов'
        ordering = ('-created_at',)

    post_id = models.ForeignKey(Post, related_name='post_id', on_delete=models.CASCADE, verbose_name='пост',
                                **NULLABLE)
    user_id = models.ForeignKey(HubUser, related_name='post_karma', on_delete=models.CASCADE,
                                verbose_name='пользователь', **NULLABLE)
    karma = models.SmallIntegerField(verbose_name='карма', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add=True)

    def __str__(self):
        return f'{self.user_id} - "{self.post_id}": {self.karma}'


class Comment(models.Model):
    class Meta:
        db_table = "comments"

    path = models.TextField()
    comment_post_id = models.ForeignKey(Post, related_name='comment_post_id', verbose_name='пост',
                                        on_delete=models.CASCADE,
                                        **NULLABLE)
    author_id = models.ForeignKey(HubUser, related_name='author_id', verbose_name='пользователь',
                                  on_delete=models.CASCADE,
                                  **NULLABLE)
    content = models.TextField(verbose_name='комментарий')
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add=True)

    def __str__(self):
        return self.content[0:200]

    def get_offset(self):
        path = json.loads(self.path)
        level = len(path) - 1
        if level > 5:
            level = 5
        return level

    def get_col(self):
        path = json.loads(self.path)
        level = len(path) - 1
        if level > 5:
            level = 5
        return 12 - level

    def get_absolute_url(self):
        print(f'self.comment_post_id.pk: {self.comment_post_id.pk}')
        print(f'self.pk: {self.pk}')
        print(f'self.__dict__: {self.__dict__}')
        return f'/post/{self.comment_post_id.pk}/'

