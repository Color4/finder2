# coding=utf-8
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
from django.conf import settings
import finder.views as views
import finder.views
from django.views.static import serve

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', finder.views.home, name='index'),
    url(r'^add/(\d)/(\d)/$', finder.views.add),
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
    url('^some_view/', views.some_view),  # 这是打开form表单的链接
    url('^person/$', finder.views.person, name='person'),
    url('^weixin/$', finder.views.weixin, name='weixin'),
    url('^test/$', finder.views.test, name='test'),
    # bootcamp
    url(r'^feeds/', include('feed.urls')),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'core/cover.html'}, name='login'),
    url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^signup/$', 'user.views.signup', name='signup'),
    url(r'^settings/$', 'core.views.settings', name='settings'),
    url(r'^settings/picture/$', 'core.views.picture', name='picture'),
    url(r'^settings/upload_picture/$', 'core.views.upload_picture', name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', 'core.views.save_uploaded_picture', name='save_uploaded_picture'),
    url(r'^settings/password/$', 'core.views.password', name='password'),
    url(r'^network/$', 'core.views.network', name='network'),
    url(r'^questions/', include('questions.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^messages/', include('messages.urls')),
    url(r'^notifications/$', 'activities.views.notifications', name='notifications'),
    url(r'^notifications/last/$', 'activities.views.last_notifications', name='last_notifications'),
    url(r'^notifications/check/$', 'activities.views.check_notifications', name='check_notifications'),
    url(r'^search/$', 'search.views.search', name='search'),
    url(r'^(?P<username>[^/]+)/$', 'core.views.profile', name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),

]

# if settings.DEBUG:
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]