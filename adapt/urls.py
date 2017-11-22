from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'adapt.views.central', name='central'),
    url(r'^central/$', 'adapt.views.central', name='central'),
    url(r'^services/$', 'adapt.views.services', name='services'),
    url(r'^portfolios/$', 'adapt.views.portfolios', name='portfolios'),
    url(r'^contacts/$', 'adapt.views.contacts', name='contacts'),

    #url(r'^portfolio/get/(?P<project_id>\d+)/$', 'adapt.views.project', name='project'),
    url(r'^get/(?P<article_id>\d+)/$', 'adapt.views.article', name='article'),
    url(r'^services/get/(?P<service_id>\d+)/$', 'adapt.views.service', name='service'),

    #url(r'^page/(\d+)/$', 'adapt.views.portfolio', name='portfolio'),
    url(r'^page_pro/(\d+)/$', 'adapt.views.central', name='central')

    ]