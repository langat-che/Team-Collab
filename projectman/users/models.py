from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description=models.TextField(blank=True, null=True,)
    
    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='profile_image/', blank=True, null=True, default='default.jpg')
    role = models.CharField(blank=True, null=True, max_length=255)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(null=True,blank=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.session_key}"
    
