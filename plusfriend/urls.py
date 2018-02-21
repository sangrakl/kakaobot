from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^keyboard$', views.keyboard),
    url(r'^message$', views.keyboard),
]
