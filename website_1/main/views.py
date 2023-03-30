from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index (request):
    tasks = Task.objects.all()
    return render (request, 'index.html', {'title':'Главная страница', 'tasks': tasks})

def about (request):
    return render(request, 'about.html ')

def homework (reqest):
    return HttpResponse ('<h1> Why Httpresponse, why not render????? <br> PS. Почему не сразу через render????</h1>'
                         ' <br>'
                         ' <h2> Я думал со сменой лектора хоть что то  измениться, но я ошибался (надеюсь только пока) </h2> '
                         '<br>'
                         '<h2> Пусть хотя бы шрифт у себя увеличит!!!!! <br> (понимаю что мне уже не поможет, но хоть следующим)</h2> '
                         '<h1><b> !!!!!ОРУУУУУУ В ГОЛОС!!!! </h1>')

def homework_2(request):
    return render (request, 'homework_2.html')

