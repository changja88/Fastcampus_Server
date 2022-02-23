from django.db import models
from django.db.models import FileField, ImageField


class Youtube(models.Model):
    title = models.TextField(null=False, blank=False, default="")
    content = models.TextField(null=False, blank=False, default="")
    video = FileField(upload_to='Youtube')
    thumbnail = ImageField(upload_to="Youtube_thumnail")