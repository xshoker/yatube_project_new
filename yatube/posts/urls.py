# posts/urls.py
from django.urls import path

from posts import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group),
    path('group/<slug:pk>/', 
    views.group_posts),
]