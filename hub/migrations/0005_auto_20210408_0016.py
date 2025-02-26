# Generated by Django 3.1.7 on 2021-04-07 21:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0004_hubcategoryusers_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hub',
            options={'ordering': ('-created_at',), 'verbose_name': 'Поток', 'verbose_name_plural': 'Потоки'},
        ),
        migrations.AlterModelOptions(
            name='hubcategory',
            options={'ordering': ('-created_at',), 'verbose_name': 'Хаб', 'verbose_name_plural': 'Хабы'},
        ),
        migrations.AlterModelOptions(
            name='hubcategoryusers',
            options={'ordering': ('-created_at',), 'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
        migrations.AddField(
            model_name='hub',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hub',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
        migrations.AddField(
            model_name='hubcategoryusers',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hubcategoryusers',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
    ]
