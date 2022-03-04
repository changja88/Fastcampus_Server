from django.contrib.auth.models import User
from django.db import models


class ToDo(models.Model):
    user = models.ForeignKey(User, related_name='to_do', on_delete=models.CASCADE, null=False)
    content = models.TextField(blank=False, null=False, max_length=200)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_created=True,auto_now_add=True)

