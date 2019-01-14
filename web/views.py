from django.shortcuts import render

def home(request):
    return render(request, 'web/home.html')

def bio(request):
    return render(request, 'web/bio.html')