from django.core.management.base import BaseCommand
from django.utils import timezone
from tasks.models import Task
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Checks for tasks that are almost due and sends alerts'

    def handle(self, *args, **options):
        almost_due_tasks = Task.objects.filter(due_date__lte=timezone.now() + timezone.timedelta(days=2))

        for task in almost_due_tasks:
            self.send_alert(task)

    def send_alert(self, task):
        subject = f"Task '{task.task_name}' is almost due"
        message = f"Hello {task.assigned_to.first_name},\n\nThis is a reminder that task '{task.task_name}' is almost due. Please complete it by {task.due_date}.\n\nBest regards,\nYour App"
        recipient_list = [task.assigned_to.email]

        send_mail(subject, message, None, recipient_list)
        self.stdout.write(self.style.SUCCESS(f"Alert sent to {task.assigned_to.username} for task '{task.task_name}'."))