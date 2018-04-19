# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from models import *
from .forms import *
from django.utils import timezone

# Create your views here.

def home_page(request):
    if request.method == 'GET':
        # product_list = Products.objects.filter(posted_on__lte=timezone.now()).order_by('-posted_on')
        product_latest = Products.objects.filter(posted_on__lte=timezone.now()).order_by('-id')[:8]
        cat = Category.objects.all()
        blog = Home_blog.objects.filter(posted_on__lte=timezone.now()).order_by('-posted_on').order_by('-id')[:3]

        context = {
            # 'product_list': product_list,
            'product_latest': product_latest,
            'cat': cat,
            'blog': blog,


        }
        return render(request, 'home/index.html', context)



def product_category(request, name=None):
    # product_list = Products.objects.filter(posted_on__lte=timezone.now()).order_by('-posted_on')
    product_latest = Products.objects.filter(posted_on__lte=timezone.now()).order_by('-id')[:8]
    cat = Category.objects.all()
    blog = Home_blog.objects.filter(posted_on__lte=timezone.now()).order_by('-posted_on').order_by('-id')[:3]
    this_cat = get_object_or_404(cat, name=name)
    posts_cat = Products.objects.filter(category=this_cat.id).filter(posted_on__lte=timezone.now()).order_by('-posted_on').order_by('-id')[:8]



    context = {
        # 'product_list': product_list,
        'product_latest': posts_cat,
        'cat': cat,
        'blog': blog,
        'current_category': name,

    }
    return render(request, 'home/index.html', context)





def shop_page(request):
    if request.method == 'GET':
        product_list = Products.objects.filter(posted_on__lte=timezone.now()).order_by('-posted_on')
        cat = Category.objects.all()
        context = {
            'product_list': product_list,
            'cat': cat,


        }
        return render(request, 'home/shop.html', context)


def shop_product_category(request, name=None):
    product_list = Products.objects.filter(posted_on__lte=timezone.now()).order_by('-posted_on')
    cat = Category.objects.all()
    blog = Home_blog.objects.all()
    this_cat = get_object_or_404(cat, name=name)
    posts_cat = Products.objects.filter(category=this_cat.id).filter(posted_on__lte=timezone.now()).order_by('-posted_on')



    context = {
        'product_list': posts_cat,
        'cat': cat,
        'blog': blog,
        'current_category': name,

    }
    return render(request, 'home/shop.html', context)


def about_page(request):
        return render(request, 'home/about.html')

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            print 'saved'
            return render(request, 'home/index.html')
        else:
            print 'error sent'
            return render(request, 'home/index.html', {'form' : form, 'contact' : True })
    else:
        print 'nothing'
        return render(request, 'home/index.html', { 'contact' : True })