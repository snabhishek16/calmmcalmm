# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Gender_category(models.Model):
        name = models.CharField(max_length=5)

        def __unicode__(self):
            return self.name

class Products(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=2000)
    image = models.FileField(upload_to='products/%Y/%m/%d/')
    category = models.ForeignKey(Category, null=True)
    gender_category = models.ForeignKey(Gender_category, null=True)
    original_price = models.DecimalField( max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)


    def __unicode__(self):
        return self.title





