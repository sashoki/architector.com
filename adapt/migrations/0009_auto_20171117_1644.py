# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-17 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import mptt.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('adapt', '0008_auto_20161018_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='adapt.Category', verbose_name='\u0411\u0430\u0442\u044c\u043a\u0456\u0432\u0441\u044c\u043a\u0438\u0439 \u043a\u043b\u0430\u0441')),
            ],
            options={
                'ordering': ('tree_id', 'level'),
                'db_table': 'category',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_title', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u043e\u0431\u0454\u043a\u0442\u0443')),
                ('port_img', models.ImageField(upload_to='portfolio/', verbose_name='\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f')),
                ('port_text', tinymce.models.HTMLField(verbose_name='\u041e\u043f\u0438\u0441 \u043e\u0431\u0454\u043a\u0442\u0443')),
                ('port_video', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='\u0412\u0456\u0434\u0435\u043e')),
                ('port_data', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0456\u043d\u0447\u0435\u043d\u043d\u044f \u0440\u043e\u0431\u0456\u0442')),
                ('port_client', models.CharField(max_length=200, verbose_name='\u0406\u043c\u044f \u043a\u043b\u0456\u0454\u043d\u0442\u0430')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='adapt.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f \u0440\u043e\u0431\u0456\u0442')),
            ],
            options={
                'ordering': ['-port_data'],
                'db_table': 'Portfolio',
                'verbose_name': '\u041f\u043e\u0440\u0442\u0444\u043e\u043b\u0456\u043e',
                'verbose_name_plural': '\u041f\u043e\u0440\u0442\u0444\u043e\u043b\u0456\u043e',
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_uset',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]