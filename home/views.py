# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from models import *
from django.utils import timezone

# Create your views here.

def home_page(request):
    if request.method == 'GET':
        product_list = Products.objects.all()
        product_latest = Products.objects.filter(posted_on__lte=timezone.now()).order_by('-id')[:4]
        cat = Category.objects.all()
        blog = Home_blog.objects.all()
        print blog


        context = {
            'product_list': product_list,
            'product_latest': product_latest,
            'cat': cat,
            'blog': blog,


        }
        return render(request, 'home/index.html', context)


# def products_list(request):
#
#
#     return render(request, 'home/index.html', context)

def product_category(request, name=None):
    product_list = Products.objects.all()
    product_latest = Products.objects.filter(posted_on__lte=timezone.now()).order_by('-id')[:4]
    cat = Category.objects.all()
    blog = Home_blog.objects.all()
    this_cat = get_object_or_404(cat, name=name)
    posts_cat = Products.objects.filter(category=this_cat.id)



    context = {
        'product_list': posts_cat,
        'product_latest': product_latest,
        'cat': cat,
        'blog': blog,
        'current_category': name,

    }
    return render(request, 'home/index.html', context)





