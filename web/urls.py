#coding=utf-8
"""xiaobaifinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import finder.views as views
import registration.backends.hmac
from django.contrib.auth.views import login, logout
import finder.views


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$|^index/$', views.home, name='index'),
    url(r'^add/(\d)/(\d)/$', views.add),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^accounts/', include('registration.backends.hmac.urls')),
    url('^accounts/', include('registration.backends.hmac.urls')),
    # url(r'^form/$', finder.views.form),
    url(r'^contactform/$', views.contact_author, name='contactform'),
    # url(r'^post/$', finder.views.post, name='post'),
    url(r'^db/$', views.db),
    url(r'^books/$', views.book_list, name='books'),
    url(r'^captcha/', include('captcha.urls')),
    url('^wordcloud/', views.word_cloud, name='word_cloud'),
    url('^userprofile/', views.user_profile, name='user_profile'),
    url('^ajax_val/', views.ajax_val, name='ajax_val'),
    url('^some_view/', views.some_view), # 这是打开form表单的链接
    url('^person/$', finder.views.person, name = 'person'),
    url('^weixin/$', finder.views.weixin, name = 'weixin')
    # url(r'^grappelli/', include('grappelli.urls')),

]
