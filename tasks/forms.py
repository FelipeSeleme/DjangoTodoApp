from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'complete']  # Garantir que 'complete' esteja aqui

    complete = forms.BooleanField(required=False, widget=forms.CheckboxInput)
