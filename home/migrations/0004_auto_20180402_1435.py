# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_home_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='content',
        ),
        migrations.RemoveField(
            model_name='products',
            name='original_price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='selling_price',
        ),
    ]
