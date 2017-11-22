# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 12:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_title', models.CharField(max_length=200)),
                ('data_img', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('data_text', models.TextField()),
            ],
            options={
                'db_table': 'data',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('project_img', models.ImageField(help_text='150x150px', upload_to='img/', verbose_name='\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f')),
                ('project_text', models.TextField()),
                ('project_data', models.DateTimeField()),
                ('project_uset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]