# Generated by Django 3.1.7 on 2021-04-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_auto_20210424_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='post.Tags', verbose_name='тэги поста'),
        ),
    ]
