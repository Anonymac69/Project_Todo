from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
