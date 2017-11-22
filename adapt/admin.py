# -*- coding: utf-8 -*-

from django.contrib import admin
from adapt.models import Data, Portfolio, Category, Article, Service

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_title', 'article_img', 'article_data']
    list_filter = ['article_data']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_title', 'service_img', 'service_data']
    list_filter = ['service_data']

class PortfolioAdmin(admin.ModelAdmin):
    fields = ['port_title', 'port_img', 'port_text', 'port_video', 'port_data', 'port_client', 'category']
    list_display = ('port_title', 'port_data', 'port_img', 'category')
    list_filter = ['category']
    search_fields = ['port_title']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']

class DataAdmin(admin.ModelAdmin):
    list_display = ['data_title', 'data_text', 'data_img']


admin.site.register(Article,  ArticleAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Data, DataAdmin)