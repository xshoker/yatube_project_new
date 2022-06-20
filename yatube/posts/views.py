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
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'posts/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Yatube для друзей'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Главная страница',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)

# Страница со списком мороженого
def group(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'posts/group.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = '"Здесь будет информация о группах проекта Yatube"'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': '"Здесь будет информация о группах проекта Yatube"',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)

# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request, pk):
    return HttpResponse(f'Пост номер {pk}')