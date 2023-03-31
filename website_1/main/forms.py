from .models import Task
from django.forms import ModelForm, TextInput, DateField, DateInput, Textarea




class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task','deadline']
        widgets = {"title": TextInput(attrs={"class": "form-control", "placeholder": "Введите название"}),
                   "task": Textarea (attrs={"class": "form-control", "placeholder":"Введите описание"}),
                   "deadline": DateInput (attrs={"class":"form-control-s", 'placeholder': "дата завершения"})

                   }
