from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index,name = 'home'),
        path('homework/', views.homework),
        path('about/', views.about,name = 'about' ),
        path('homework_2/', views.homework_2),
        path('create/', views.create,name = 'create'),

]