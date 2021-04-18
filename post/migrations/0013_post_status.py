# Generated by Django 3.1.7 on 2021-04-18 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_remove_post_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'опубликован'), ('unpublished', 'неопубликован'), ('archive', 'в архиве')], default='unpublished', max_length=11, verbose_name='статус'),
        ),
    ]
