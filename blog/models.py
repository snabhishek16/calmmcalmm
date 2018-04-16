# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Blog(models.Model):
    username = models.CharField(max_length=20)
    user_image = models.FileField(upload_to='user/%Y/%m/%d/')
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=2000)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)


    def __unicode__(self):
        return self.title