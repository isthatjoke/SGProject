from django.contrib.auth.models import User
from django.db import models

NULLABLE = {'blank': True, 'null': True}
# Create your models here.


class Hub(models.Model):
    name = models.CharField(max_length=150, verbose_name='название',)
    description = models.CharField(max_length=500, verbose_name='описание', **NULLABLE,)


class HubCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='название',)
    short_desc = models.CharField(max_length=150, verbose_name='краткое описание',)
    description = models.CharField(max_length=500, verbose_name='описание', **NULLABLE,)
    tags = models.CharField(max_length=300, verbose_name='тэги', **NULLABLE,)
    category = models.ForeignKey(Hub, related_name='categories', verbose_name='категории', on_delete=models.CASCADE,
                                 **NULLABLE)
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add=True,)
    updated_at = models.DateTimeField(verbose_name='время обновления', auto_now=True,)


class HubCategoryUsers(models.Model):
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    hub_category = models.ForeignKey(HubCategory, related_name='hubs', on_delete=models.CASCADE,)

    @staticmethod
    def get_category_users(pk):
        return HubCategoryUsers.objects.filter(hub_category=pk).count()

