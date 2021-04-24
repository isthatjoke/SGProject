from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

NULLABLE = {'blank': True, 'null': True}


class HubUser(AbstractUser):

    BANNED_FALSE = 'active'
    BANNED_FOR_TIME = 'banned_for_time'
    BANNED_FOREVER = 'banned_forever'

    BANNED_STATUSES = (
        (BANNED_FALSE, 'активный'),
        (BANNED_FOR_TIME, 'временно забанен'),
        (BANNED_FOREVER, 'перманентно забанен'),
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-created_at',)

    avatar = models.ImageField(verbose_name='аватарка', upload_to='avatars', blank=True)
    age = models.IntegerField(verbose_name='возраст', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='зарегистрирован', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    banned = models.CharField(max_length=15, choices=BANNED_STATUSES, default=BANNED_FALSE, verbose_name='забанен')
    banned_to = models.DateTimeField(verbose_name='забанен до', **NULLABLE)
    rating = models.PositiveSmallIntegerField(verbose_name='рейтинг пользователя', default=0)


class HubUserProfile(models.Model):

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ('-created_at',)

    MALE = 'M'
    FEMALE = 'F'

    SEX_CHOICES = (
        (MALE, 'м'),
        (FEMALE, 'ж'),
    )

    user = models.OneToOneField(HubUser, on_delete=models.CASCADE, unique=True, db_index=True)
    specialization = models.CharField(verbose_name='специализация', max_length=150, **NULLABLE)
    name = models.CharField(verbose_name='имя', max_length=150, **NULLABLE)
    sex = models.CharField(verbose_name='пол', choices=SEX_CHOICES, max_length=1, **NULLABLE)
    birthdate = models.DateField(verbose_name='день рождения', **NULLABLE)
    location = models.CharField(verbose_name='страна', max_length=50, **NULLABLE)
    location_city = models.CharField(verbose_name='город', max_length=100, **NULLABLE)
    created_at = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлен', auto_now=True)

    @receiver(post_save, sender=HubUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            HubUserProfile.objects.create(user=instance)

    # @receiver(post_save, sender=HubUser)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.hubuserprofile.save()

    def __str__(self):
        return f'{self.user}'


