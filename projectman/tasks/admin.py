from django.contrib import admin
from .models import Project, Task, Announcement, Comment, Travel, Attachment

# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Announcement)
admin.site.register(Comment)
admin.site.register(Travel)
admin.site.register(Attachment)