# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from home.models import *
from django.shortcuts import render

# Create your views here.

def blog_page (request):
    if request.method == 'GET':
        blog = Home_blog.objects.all()

        context = {
            'blog': blog,
        }
        return render(request, 'blog/blog.html', context)