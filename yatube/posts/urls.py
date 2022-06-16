# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', include('posts.urls')),
    path('group', views.group),
    path('group/<slug:slug>', views.group_posts),

]