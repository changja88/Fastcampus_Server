from django.db import models


class JsonTest(models.Model):
    name = models.TextField(max_length=100, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    intro = models.TextField(max_length=300, blank=True, null=True)
