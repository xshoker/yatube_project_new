# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group),
    path('group/<int:pk>/', 
    views.group_posts),
]