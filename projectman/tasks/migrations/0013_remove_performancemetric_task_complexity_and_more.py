# Generated by Django 5.0.1 on 2024-04-16 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_alter_project_description_alter_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performancemetric',
            name='task_complexity',
        ),
        migrations.RemoveField(
            model_name='performancemetric',
            name='task_duration',
        ),
        migrations.RemoveField(
            model_name='performancemetric',
            name='task_importance',
        ),
        migrations.RemoveField(
            model_name='performancemetric',
            name='task_outcome',
        ),
    ]
