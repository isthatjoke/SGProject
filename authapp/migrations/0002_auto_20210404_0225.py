# Generated by Django 3.1.7 on 2021-04-03 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hubuser',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='hubuserprofile',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='день рождения'),
        ),
        migrations.AlterField(
            model_name='hubuserprofile',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='hubuserprofile',
            name='location_city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='город'),
        ),
        migrations.AlterField(
            model_name='hubuserprofile',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='hubuserprofile',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'м'), ('F', 'ж')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='hubuserprofile',
            name='specialization',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='специализация'),
        ),
    ]
