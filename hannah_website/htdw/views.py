from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'htdw/index.html')

def home(request):
    return render(request, 'htdw/home.html')

def about(request):
    return render(request, 'htdw/about.html')

def artist_statement(request):
    return render(request, 'htdw/artist_statement.html')

def performance(request):
    return render(request, 'htdw/performance.html')

def film(request):
    return render(request, 'htdw/film.html')

def work(request):
    return render(request, 'htdw/work.html')

def social_practice(request):
    return render(request, 'htdw/social_practice.html')

def harmless(request):
    return render(request, 'htdw/harmless.html')

def cv(request):
    return render(request, 'htdw/cv.html')

def contact(request):
    return render(request, 'htdw/contact.html')
