from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import date
import datetime
import os
import pathlib


def home_view(request):
    # return HttpResponse('Здесь будет сайт!')
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().time().replace(microsecond=0)
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    # files = os.listdir()
    # msg = f'Список файлов в рабочей директории: {files}'
    # return HttpResponse(msg)
    current_dir = os.listdir(path=pathlib.Path(__file__).parent.absolute())
    msg = f'Список файлов в рабочей директории: {current_dir}'
    return HttpResponse(msg)


