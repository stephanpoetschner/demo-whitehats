from django.db import models
from django.utils import timezone


class ConsoleLog(models.Model):
    stdout = models.TextField(default='')
    owner = models.ForeignKey('auth.User')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.created)