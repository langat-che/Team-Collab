from django import forms
from django.contrib.auth.models import User
from .models import Project, Task, Comment, PerformanceMetric, TaskStatus


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

class TaskProgressUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status', 'progress']
        
        widgets = {
            'status' : forms.Select(choices=TaskStatus,attrs={'class': 'form-select'}),
            'progress': forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': 0, 'max': 100,'oninput': 'updateTextInput(this.value)'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        
        widgets = {
            'comment_text' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class PerformanceMetricForm(forms.ModelForm):
    
    timeliness = forms.IntegerField(label='Timeliness', min_value=1, max_value=10, widget=forms.NumberInput(attrs={'type': 'range', 'class': 'form-range'}))
    quality_of_work = forms.IntegerField(label='Quality of Work', min_value=1, max_value=10, widget=forms.NumberInput(attrs={'type': 'range', 'class': 'form-range'}))
    task_difficulty_rating = forms.IntegerField(label='Task Difficulty', min_value=1, max_value=10, widget=forms.NumberInput(attrs={'type': 'range', 'class': 'form-range'}))
    
    class Meta:
        model = PerformanceMetric
        fields = ['user','task', 'timeliness', 'quality_of_work', 'task_difficulty_rating','feedback']
        
        widgets = {
            'user' : forms.Select(choices=User,attrs={'class':'form-select'}),
            'task' : forms.Select(choices=Task,attrs={'class':'form-select'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control'}),
            'user_engagement': forms.TextInput(attrs={'class': 'form-control'}),
        }
        