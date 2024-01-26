from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='profile_image/', blank=True, null=True, default='default.jpg')
    bio = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path) # Open image

    #     # resize image
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size) # Resize image
    #         img.save(self.image.path) # Save it again and override the larger image


