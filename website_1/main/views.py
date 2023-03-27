from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse ("<h4> This is index page </h4> <br> "
                         "<p><a href='/homework'>Домашняя работа</a></p>")

def homework (reqest):
    return HttpResponse ('<h1> Why Httpresponse, why not render?????</h1>'
                         ' <br>'
                         ' <h2> Я думал со сменой лектора хоть что то  измениться, но я ошибался (надеюсь только пока </h2> '
                         '<br>'
                         '<h2> Пусть хотя бы шрифт у себя увеличит!!!!! </h2> '
                         '<h1><b> !!!!!ОРУУУУУУ В ГОЛОС!!!! </h1>')

