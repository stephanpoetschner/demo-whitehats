from django.db import models


class SignupUser(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

