from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render (request, 'index.html')

def homework (reqest):
    return HttpResponse ('<h1> Why Httpresponse, why not render????? <br> PS. Почему не сразу через render????</h1>'
                         ' <br>'
                         ' <h2> Я думал со сменой лектора хоть что то  измениться, но я ошибался (надеюсь только пока) </h2> '
                         '<br>'
                         '<h2> Пусть хотя бы шрифт у себя увеличит!!!!! <br> (понимаю что мне уже не поможет, но хоть следующим)</h2> '
                         '<h1><b> !!!!!ОРУУУУУУ В ГОЛОС!!!! </h1>')

