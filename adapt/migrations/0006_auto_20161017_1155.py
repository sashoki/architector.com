# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-17 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adapt', '0005_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-article_data'], 'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u0438', 'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438'},
        ),
    ]
