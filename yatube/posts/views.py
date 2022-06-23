from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

# posts/views.py
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 
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
def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)