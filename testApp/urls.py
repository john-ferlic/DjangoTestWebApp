# from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url('create', views.index, name='index'),
    url('show', views.show_post, name='show_post'),
    url('header', views.header, name='header')
]