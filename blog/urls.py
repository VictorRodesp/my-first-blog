# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:20:23 2020

@author: victo
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]