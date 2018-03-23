# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse

from . import models

def index (request):
    articles = models.Article.objects.all()
    return render(request, 'my_app/index.html', {"articles":articles })

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'my_app/article_page.html',{"article":article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request, 'my_app/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'my_app/edit_page.html', {"article":article })

def edit_action(request):
    tittle = request.POST.get('tittle','TITTLE')
    content=request.POST.get('content','CONTENT')
    article_id=request.POST.get('article_id','0')

    if str(article_id) == '0':
        models.Article.objects.create(tittle=tittle,content=content)
        articles = models.Article.objects.all()
        return render(request, 'my_app/index.html', {"articles":articles })
    article = models.Article.objects.get(pk=article_id)
    article.tittle = tittle
    article.content = content
    article.id = article_id
    article.save()
    return render(request,'my_app/article_page.html',{"article":article})




