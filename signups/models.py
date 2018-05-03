from django.db import models
from django.utils.translation import ugettext_lazy as _


class SignupUser(models.Model):
    email = models.EmailField(
        _('Your Email'),
        help_text=_('We will keep you updated about new releases.'))

    def __str__(self):
        return self.email

