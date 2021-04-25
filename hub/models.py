from django.contrib.auth.models import User
from django.db import models

from authapp.models import HubUser

NULLABLE = {'blank': True, 'null': True}


# Create your models here.


class Hub(models.Model):

    class Meta:
        verbose_name = 'Поток'
        verbose_name_plural = 'Потоки'
        ordering = ('-created_at',)

    name = models.CharField(max_length=150, verbose_name='название', )
    description = models.CharField(max_length=500, verbose_name='описание', **NULLABLE, )
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add=True, )
    updated_at = models.DateTimeField(verbose_name='время обновления', auto_now=True, )


class HubCategory(models.Model):

    class Meta:
        verbose_name = 'Хаб'
        verbose_name_plural = 'Хабы'
        ordering = ('-created_at',)

    name = models.CharField(max_length=150, verbose_name='название', )
    short_desc = models.CharField(max_length=150, verbose_name='краткое описание', )
    description = models.CharField(max_length=500, verbose_name='описание', **NULLABLE, )
    tags = models.CharField(max_length=300, verbose_name='тэги', **NULLABLE, )
    category = models.ForeignKey(Hub, related_name='categories', verbose_name='категории', on_delete=models.CASCADE,
                                 **NULLABLE)
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add=True, )
    updated_at = models.DateTimeField(verbose_name='время обновления', auto_now=True, )

    def __str__(self):
        return f'{self.name}'


class HubCategoryUsers(models.Model):

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-created_at',)

    user = models.ForeignKey(HubUser, related_name='users', on_delete=models.CASCADE, **NULLABLE)
    hub_category = models.ForeignKey(HubCategory, related_name='hubs', on_delete=models.CASCADE, )
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add=True, )
    updated_at = models.DateTimeField(verbose_name='время обновления', auto_now=True, )

    @staticmethod
    def get_category_users(pk):
        return HubCategoryUsers.objects.filter(hub_category=pk).count()


def get_hub_cats_dict():
    '''
    Функция формирует словарь result_dict, ключи словаря - это имена хабов,
    значения - это объекты категорий хабов
    :return: result_dict={'hub.name': HubCategoryObjects,....}
    '''
    result_dict = {}
    hubs = Hub.objects.all()
    for k in hubs:
        list_cats = []
        hubcats = HubCategory.objects.filter(category=k.id)
        list_cats.append(hubcats)
        result_dict[k] = list_cats
    return result_dict
