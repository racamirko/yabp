"""u02_blog URL Configuration

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
from devblog import views

urlpatterns = [
    url(r'^rooter/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^story/(?P<story_id>[0-9]+)/$', views.print_story, name='story'),
    url(r'^tag/(?P<tag_id>[0-9]+)/(?P<tag_name>.+)$', views.show_tag, name='tag'),
    url(r'^ajax/ajax_get_more_stories/(?P<story_offset>[0-9]+)/(?P<num_stories>[0-9]+)/$', views.ajax_get_more_stories, name='story_ajax'),
    url(r'^vrata/$', views.login_form, name='login_form'),
    url(r'^kljuc_u_bravu/$', views.login_procedure, name='login_procedure'),
    url(r'^aj_zdravo/$', views.logout_procedure, name='logout_procedure'),
]
