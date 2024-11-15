# Generated by Django 5.0.1 on 2024-04-16 08:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_alter_project_status_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=3000, null=True),
        ),
    ]
