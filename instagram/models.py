from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='Post', blank=True, null=True)
    like_count = models.PositiveIntegerField(default=0)

