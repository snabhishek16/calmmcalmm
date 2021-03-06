"""hl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views





urlpatterns = [
    url(r'^$', blog_views.blog_page,name='blogs'),
    # url(r'^(?P<id>\d+)/$', article,name='article'),
    # url('^search/', search_blog, name='search_blog'),
    # url('(?P<name>[\w-]+)/$', search_category, name='search_category')


]