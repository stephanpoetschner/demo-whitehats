from django import forms

from . import models


class SignupUserForm(forms.ModelForm):
    class Meta:
        model = models.SignupUser
        fields = ['email', ]
