from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
# ice_cream/views.py
from django.http import HttpResponse

# Главная страница
from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader


def index(request):
    template = 'posts/index.html'
    return render(request, template)

# Страница со списком мороженого
def group(request):
    return HttpResponse('Список постов')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request, pk):
    return HttpResponse(f'Пост номер {pk}')