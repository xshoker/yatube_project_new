# posts/urls.py
from django.urls import path

from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group, name='group'),
    path('group/<slug:pk>/', 
    views.group_posts),
]