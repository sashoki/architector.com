# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from embed_video.fields import EmbedVideoField
import mptt
from mptt.models import MPTTModel, TreeForeignKey

SHORT_TEXT_LEN = 500


class Article(models.Model):
    class Meta():
        ordering = ['-article_data']
        db_table = 'article'
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статьи'
    article_title = models.CharField(max_length=200)
    article_img = models.ImageField(upload_to="img/", verbose_name='Зображення', help_text="150x150px")
    article_data = models.DateTimeField()
    article_text = HTMLField()

    def __unicode__(self):
        return self.article_title

    def __str__(self):
        return self.article_title

    def get_short_text(self):
        if len(self.article_text) > SHORT_TEXT_LEN:
            return self.article_text[: SHORT_TEXT_LEN]
        else:
            return self.article_text

class Service(models.Model):
    class Meta():
        db_table = 'service'
        verbose_name_plural = 'Послуги'
        verbose_name = 'Послуги'
    service_title = models.CharField(max_length=200)
    service_img = models.ImageField(upload_to="img/", verbose_name='Зображення', help_text="150x150px")
    service_data = models.DateTimeField()
    service_text = HTMLField()

    def __unicode__(self):
        return self.service_title

    def __str__(self):
        return self.service_title

    def get_short_text(self):
        if len(self.service_text) > SHORT_TEXT_LEN:
            return self.service_text[: SHORT_TEXT_LEN]
        else:
            return self.service_text


class Data(models.Model):
    class Meta():
        db_table = 'data'
        verbose_name_plural = 'Дані'
        verbose_name = 'Дані'
    data_title = models.CharField(max_length=200)
    data_img = models.ImageField(null=True, blank=True)
    data_text = HTMLField()

    def __unicode__(self):
        return self.data_title

    def __str__(self):
        return self.data_title


class Category(MPTTModel):
    class Meta():
        db_table = 'category'
        verbose_name_plural = 'Категорії'
        verbose_name = 'Категорія'
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=150, verbose_name = 'Категорія')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'Батьківський клас')

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

mptt.register(Category, order_insertion_by=['name'])


class Portfolio(models.Model):
    class Meta():
        ordering = ['-port_data']
        db_table = 'Portfolio'
        verbose_name_plural = 'Портфоліо'
        verbose_name = 'Портфоліо'

    port_title = models.CharField(max_length=200, verbose_name=u'Назва обєкту')
    port_img = models.ImageField(upload_to="portfolio/", verbose_name='Зображення')
    port_text = HTMLField(verbose_name=u'Опис обєкту')
    port_video = EmbedVideoField(null=True, blank=True, verbose_name=u'Відео')
    port_data = models.DateTimeField(verbose_name=u'Дата закінчення робіт')
    port_client = models.CharField(max_length=200, verbose_name=u'Імя клієнта')
    category = TreeForeignKey(Category, blank=True, null=True, related_name='cat', verbose_name=u'Категорія робіт')

    def __unicode__(self):
        return self.port_title

    def __str__(self):
        return self.port_title

    def bit(self):
        if self.port_img:
            return u'<img src="%s" width="70"/>' % self.port_img.url
        else:
            return '(none)'

    bit.short_description = u'Зображення'
    bit.allow_tags = True
