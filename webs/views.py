from django.shortcuts import render
from .models import Content
from django.http import HttpResponse

def homepage(request):
    content = Content.objects.get(id=1)
    return render(request, 'webs/new_index.html', {'content': content}) 
    
def music(request):
    return render(request, 'webs/music.html')
