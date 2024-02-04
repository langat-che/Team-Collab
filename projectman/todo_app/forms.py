from django import forms
from django.contrib.auth.models import User
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title','description')
        
        widgets = {
            'title': forms.TextInput(attrs={"class":'form-control'}),
            'description': forms.Textarea(attrs={"class":'form-control'}),
        }