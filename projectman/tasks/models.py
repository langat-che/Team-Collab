from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=255)
    description = RichTextField(max_length=3000,null=True, blank=True,validators=[MinLengthValidator(100, message="Content must be at least 100 characters.")])
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('completed', 'Completed'), ('on_hold', 'On Hold')],default='active')
    project_file = models.FileField(blank=True, null=True)
    project_repo = models.URLField(blank=True, null= True)
    
    def __str__(self):
        return str(self.project_name)
   

class Task(models.Model):
    task_name = models.CharField(max_length=255, blank=True, null = True)
    description = RichTextField(max_length=3000,null=True, blank=True,validators=[MinLengthValidator(100, message="Content must be at least 100 characters.")])
    start_date = models.DateField( blank=True, null = True)
    due_date = models.DateField( blank=True, null = True)
    status = models.CharField(max_length=20, choices=[('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='not_started')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    
    def __str__(self):
        return str(self.task_name)


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_text = models.TextField()
    
    def __str__(self):
        return str(self.author)
    

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)
    
