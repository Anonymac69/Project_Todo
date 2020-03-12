from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    item = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)
