# Generated by Django 3.1.7 on 2021-04-08 20:04

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210408_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
