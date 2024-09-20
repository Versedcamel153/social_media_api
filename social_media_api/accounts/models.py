from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=250)
    profile_pic = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
