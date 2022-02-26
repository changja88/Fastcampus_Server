from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to='Profile', blank=True, null=True)
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE, null=False)