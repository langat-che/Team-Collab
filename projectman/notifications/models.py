from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class NotificationType(models.TextChoices):
    EMAIL = 'EMAIL', 'Email'
    PUSH = 'PUSH', 'Push Notification'
    IN_APP = 'IN_APP', 'In-App Notification'

class NotificationStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    SENT = 'SENT', 'Sent'
    FAILED = 'FAILED', 'Failed'

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NotificationType.choices)
    status = models.CharField(max_length=20, choices=NotificationStatus.choices, default=NotificationStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)