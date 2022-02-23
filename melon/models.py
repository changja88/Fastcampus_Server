from django.db import models

# Create your models here.
from django.db.models import FileField


class Melon(models.Model):
    title = models.TextField(null=False, blank=False, max_length=200)
    song = FileField(upload_to="melon")
    thumbnail = FileField(upload_to="melon")
