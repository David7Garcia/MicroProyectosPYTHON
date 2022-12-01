from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def hello(request, username):
    print(type(username))
    return HttpResponse("<h1>Hello %s </h1>" % username)

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')


def task(request,tittle):
    task= get_object_or_404(Task, tittle=tittle)
    return render(request, 'task.html')