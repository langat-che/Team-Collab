from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from .models import Notification, NotificationType
from tasks.models import Task, Project, Announcement
from django.contrib import messages

@receiver(post_save, sender=Task)
def create_task_assigned_notification(sender, instance, created, **kwargs):
    if created:
        message = f"You have been assigned a new task: '{instance.task_name}'"
        notification = Notification.objects.create(
            recipient=instance.assigned_to,
            message=message,
            notification_type=NotificationType.EMAIL,
        )

def check_task_deadlines():
    upcoming_tasks = Task.objects.filter(
        status__in=['OPEN', 'IN_PROGRESS'],
        due_date__gt=timezone.now(),
        due_date__lte=timezone.now() + timedelta(days=7)
    )
    for task in upcoming_tasks:
        message = f"Task '{task.task_name}' is due on {task.due_date.strftime('%Y-%m-%d')}"
        notification = Notification.objects.create(
            recipient=task.assigned_to,
            message=message,
            notification_type=NotificationType.EMAIL,
        )
        
@receiver(post_save, sender=Project)
def create_project_status_change_notification(sender, instance, **kwargs):
    if instance.tracker.has_changed('status'):
        assigned_users = Task.objects.filter(project=instance).values_list('assigned_to', flat=True).distinct()
        for user in assigned_users:
            message = f"The status of project '{instance.project_name}' has changed to '{instance.status}'"
            notification = Notification.objects.create(
                recipient=user,
                message=message,
                notification_type=NotificationType.EMAIL,
            )
            
User = get_user_model()

@receiver(post_save, sender=Announcement)
def create_new_announcement_notification(sender, instance, created, **kwargs):
    if created:
        users = User.objects.all()
        for user in users:
            message = f"New announcement: '{instance.title}'"
            notification = Notification.objects.create(
                recipient=user,
                message=message,
                notification_type=NotificationType.IN_APP,
            )
            