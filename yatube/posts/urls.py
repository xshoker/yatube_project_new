# posts/urls.py
from django.urls import path

from posts import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group, name = 'posts_list'),
    path('group/<slug:pk>/', 
    views.group_posts),
]