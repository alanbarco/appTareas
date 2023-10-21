from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribir el nombre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribir la descripción'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }