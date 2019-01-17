from django.shortcuts import render
from .models import Content

def home(request):
    return render(request, 'web/home.html')

def bio(request):
    return render(request, 'web/bio.html')