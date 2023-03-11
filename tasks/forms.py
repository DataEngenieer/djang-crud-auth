from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'descripcion', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
