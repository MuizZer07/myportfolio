from django.shortcuts import render
from .models import Content, Project
from django.http import HttpResponse

def homepage(request):
    content = Content.objects.get(id=1)
    return render(request, 'webs/new_index.html', {'content': content}) 
    
def my_projects(request):
    projects = Project.objects.all()
    return render(request, 'webs/my_projects.html', {'projects': projects})

def show_project(request, project_id):
    p = Project.objects.get(pk=project_id)
    return render(request, 'webs/project.html', {'project': p})

def bin(request):
    return render(request, 'webs/bin.html')
