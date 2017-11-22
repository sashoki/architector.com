# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('adapt', '0002_auto_20160715_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_text', tinymce.models.HTMLField()),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
