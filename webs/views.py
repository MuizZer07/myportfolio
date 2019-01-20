from django.shortcuts import render
from .models import Content
from django.http import HttpResponse

def homepage(request):
    content = Content.objects.get(id=1)
    return render(request, 'webs/home.html', {'content': content}) 

def biopage(request):
    content = Content.objects.get(id=1)
    bio = content.bio
    return render(request, 'webs/bio.html', {'bio': bio})

def music(request):
    return render(request, 'webs/music.html')
