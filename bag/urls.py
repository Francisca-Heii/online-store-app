
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.views_bag, name='views_bag'),
    
]
