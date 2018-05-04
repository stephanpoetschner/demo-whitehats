import logging

from django.shortcuts import render, redirect

from . import forms

logger = logging.getLogger(__name__)


def signup(request):
    form = forms.SignupUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        logger.info('New signup collected.')
        return redirect(to="success")
    return render(request, "signups/signup.html", {"signup_form": form,})


def success(request):
    return render(request, 'signups/success.html')
