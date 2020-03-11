from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    added_date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200, null='False')

    # def __str__(self):
    #     return self.title
