# Generated by Django 3.1.7 on 2021-04-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210415_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='hubuser',
            name='banned',
            field=models.CharField(choices=[('active', 'активный'), ('banned for time', 'временно забанен'), ('banned forever', 'перманентно забанен')], default='active', max_length=15, verbose_name='статус бана'),
        ),
        migrations.AddField(
            model_name='hubuser',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='рейтинг пользователя'),
        ),
    ]
