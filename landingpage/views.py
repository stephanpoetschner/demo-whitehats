from django.shortcuts import render


def home(request):
    return render(request, 'landingpage/home.html', {
        'name': 'Stephan',
    })
