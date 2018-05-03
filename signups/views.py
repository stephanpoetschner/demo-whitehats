from django.shortcuts import render


def signup(request):
    return render(request, 'signups/signup.html', {
        'name': 'Stephan',
    })
