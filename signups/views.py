from django.shortcuts import render, redirect

from . import forms


def signup(request):
    form = forms.SignupUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(to="success")
    return render(request, "signups/signup.html", {"signup_form": form,})


def success(request):
    return render(request, 'signups/success.html')
