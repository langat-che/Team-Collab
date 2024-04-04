# Generated by Django 5.0.1 on 2024-03-21 11:33

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_project_progress_task_progress'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('ready', 'Ready'), ('done', 'Done'), ('on_hold', 'On Hold'), ('blocked', 'Blocked')], default='ready', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not_started', 'Not Started'), ('done', 'Done'), ('on_hold', 'On Hold'), ('blocked', 'Blocked')], default='not_started', max_length=20),
        ),
        migrations.CreateModel(
            name='PerformanceMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeliness', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('quality_of_work', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('feedback', models.TextField(blank=True, null=True)),
                ('task_complexity', models.CharField(blank=True, max_length=50)),
                ('task_duration', models.DurationField(blank=True, null=True)),
                ('task_difficulty_rating', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('task_importance', models.CharField(blank=True, max_length=50)),
                ('task_outcome', models.CharField(blank=True, max_length=100)),
                ('user_engagement', models.CharField(blank=True, max_length=50)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]