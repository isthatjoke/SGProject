# Generated by Django 3.1.7 on 2021-05-13 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0030_auto_20210513_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentcomplaint',
            name='is_satisfied',
            field=models.BooleanField(blank=True, null=True, verbose_name='жалоба удовлетворена'),
        ),
    ]
