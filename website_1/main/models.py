from django.db import models

class Task (models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    creation_date = models.DateTimeField('Дата создания', auto_now_add= True)
    deadline = models.DateField('Срок выполнения')
    def __str__(self):
        return self.title


# Create your models here.
