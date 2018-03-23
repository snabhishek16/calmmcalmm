# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *

# Create your views here.

def home_page(request):
    if request.method == 'GET':
        return render(request, 'home/index.html')


def products_list(request):
    product_list = Products.objects.filter(publish__lte=timezone.now()).order_by('-publish')
    cat = Category.objects.all()

    context = {
        'product_list': product_list,
        'cat': cat,
    }

    return render(request, 'home/index.html', context)



