# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-19 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('user_image', models.FileField(upload_to='user/%Y/%m/%d/')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=2000)),
                ('posted_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
