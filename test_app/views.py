# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse

def index (request):
    return render(request, 'test_app/index.html', {"hello": 'hello , test_app'})


