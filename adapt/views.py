from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from adapt.models import Data, Portfolio, Article, Service, Category
from django.core.paginator import Paginator
from django.contrib import auth


# Create your views here.

def index(request):
    return render(request, 'index.html')

def central(request, page_number=1):
    all_articles = Article.objects.all()
    all_services = Service.objects.all()
    all_projects = Portfolio.objects.all()
    current_page = Paginator(all_articles, 3)
    args = {}
    args['projects'] = all_projects
    args['services'] = all_services
    args['articles'] = current_page.page(page_number)
    return render(request, 'adapt/central.html', args)


def article(request, article_id=1):
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    return render(request, 'adapt/article.html', args)

def services(request, page_number=1):
    all_services = Service.objects.all()
    current_page = Paginator(all_services, 10)
    args = {}
    args['services'] = current_page.page(page_number)
    return render(request, 'adapt/services.html', args)

def service(request, service_id=1):
    args = {}
    args.update(csrf(request))
    args['service'] = Service.objects.get(id=service_id)
    return render(request, 'adapt/service.html', args)

def portfolios(request, portfolio_id=1):
    args = {}
    args['portfolios'] = Portfolio.objects.all()
    args['portfolio'] = Portfolio.objects.get(id=portfolio_id)
    args['projects'] = Category.objects.all()
    args['category'] = Category.objects.filter(id=portfolio_id)
    return render(request, 'adapt/portfolios.html', args)

def project(request, project_id=1):
    args = {}
    args.update(csrf(request))
    args['project'] = Portfolio.objects.get(id=project_id)
    args['username'] = auth.get_user(request).username
    return render(request, 'adapt/project.html', args)


def contacts(request):
    data = Data.objects.all()
    context = {'data': data}
    return render(request, 'adapt/contacts.html', context)

