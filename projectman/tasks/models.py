from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class ProjectStatus(models.TextChoices):
    OPEN = 'OPEN', 'Open'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    BLOCKED = 'BLOCKED', 'Blocked'
    COMPLETED = 'COMPLETED', 'Completed'


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    description = RichTextField(max_length=3000,null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=ProjectStatus.choices, default=ProjectStatus.OPEN)
    project_file = models.FileField(upload_to='media/', null=True, blank=True)
    project_repo = models.URLField(blank=True, null= True)
    progress = models.IntegerField(default=0)
    
    def calculate_progress_percentage(self):
        total_tasks = self.task_set.count()
        completed_tasks = self.task_set.filter(status='Completed').count()
        if total_tasks != 0:
            self.progress_percentage = (completed_tasks / total_tasks) * 100
        else:
            self.progress_percentage = 0
        self.save()
    
    def __str__(self):
        return str(self.project_name)

class TaskStatus(models.TextChoices):
    OPEN = 'OPEN', 'Open'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    BLOCKED = 'BLOCKED', 'Blocked'
    COMPLETED = 'COMPLETED', 'Completed'

class Task(models.Model):
    task_name = models.CharField(max_length=255, null=False)
    description = RichTextField(max_length=3000,null=True, blank=True)
    start_date = models.DateField( blank=True, null = True)
    due_date = models.DateField( blank=True, null = True)
    status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.OPEN)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    progress = models.IntegerField(default=0)
    
    def calculate_progress_percentage(self):
        if self.status == 'Completed':
            self.progress_percentage = 100
        else:
            self.progress_percentage = 0
        self.save()
    
    def __str__(self):
        return str(self.task_name)

class PerformanceMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    timeliness = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    quality_of_work = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    feedback = models.TextField(blank=True, null=True)
    task_difficulty_rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    user_engagement = models.CharField(max_length=50, blank=True)

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
    
