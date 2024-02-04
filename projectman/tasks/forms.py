from django import forms
from django.contrib.auth.models import User
from .models import Project, Task, Comment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'start_date', 'end_date','project_file', 'project_repo']
        
        widgets = {
            'project_name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type':'date'}),
            'end_date': forms.DateInput(attrs={'type':'date'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'start_date', 'due_date', 'assigned_to']
        
        widgets = {
            'task_name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type':'date'}),
            'due_date': forms.DateInput(attrs={'type':'date'}),
            'assigned_to' : forms.Select(choices=User,attrs={'class': 'form-select'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        
        widgets = {
            'comment_text' : forms.Textarea(attrs={'class': 'form-control'}),
        }

 
