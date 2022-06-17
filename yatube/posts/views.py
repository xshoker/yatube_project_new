from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
# ice_cream/views.py
from django.http import HttpResponse

# Главная страница
def index(request):
    html_content = '<html><head><title>Yatube</title></head><body>'
    html_content += '<h1>Главная страница</h1>'
    html_content += '</body></html>'    
    return HttpResponse(html_content)


# Страница со списком мороженого
def group(request):
    return HttpResponse('Список постов')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request, pk):
    return HttpResponse(f'Пост номер {pk}')