from django.shortcuts import render, redirect
from .models import Content, Project, TextBin, FileBin, top10s, Ratings, Tag
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import TextForm, FileForm
from django.utils import timezone
import datetime

def homepage(request):
    content = Content.objects.get(id=1)
    now = datetime.datetime.now().strftime("%A, %B %d, %Y")
    return render(request, 'webs/new_index.html', {'content': content, 'now': now}) 
    
def my_projects(request):
    projects = Project.objects.all()
    return render(request, 'webs/my_projects.html', {'projects': projects})

def show_project(request, project_id):
    p = Project.objects.get(pk=project_id)
    return render(request, 'webs/project.html', {'project': p})

def my_top_10s(request):
    _top10s = top10s.objects.all()
    return render(request, 'webs/top10s.html', {'top10s': _top10s})

def my_ratings(request):
    ratings = Ratings.objects.order_by('-id')
    paginator = Paginator(ratings, 8)

    page = request.GET.get('page')
    ratings = paginator.get_page(page)

    return render(request, 'webs/ratings.html', {'ratings': ratings})

def bin(request):
    form = TextForm()
    file_form = FileForm()
    texts = TextBin.objects.order_by('-id')
    files = FileBin.objects.order_by('-id')
    recent_texts_list = TextBin.objects.order_by('-id')
    recent_files_list = FileBin.objects.order_by('-id')

    paginator = Paginator(recent_texts_list, 5)
    page = request.GET.get('page')
    recent_texts = paginator.get_page(page)

    paginator1 = Paginator(recent_files_list, 5)
    page1 = request.GET.get('page1')
    recent_files = paginator1.get_page(page1)
    return render(request, 'webs/bin.html', {'form':form, 'file_form':file_form, 'texts': texts, 'files': files, 'recent_texts': recent_texts, 'recent_files': recent_files})

def deletetext(request, text_id):
    instance = TextBin.objects.get(id=text_id)
    instance.delete()

    a = request.POST.get('bin', '/bin')
    return HttpResponseRedirect(a)

def deletefile(request, file_id):
    instance = FileBin.objects.get(id=file_id)
    instance.delete()

    a = request.POST.get('bin', '/bin')
    return HttpResponseRedirect(a)

def savetext(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        text = form.save(commit=False)
        text.created = timezone.now()
        text.save()

        a = request.POST.get('bin', '/bin')
        return HttpResponseRedirect(a)

def savefile(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.save(commit=False)
            file.created = timezone.now()
            file.save()
            
        a = request.POST.get('bin', '/bin')
        return HttpResponseRedirect(a)