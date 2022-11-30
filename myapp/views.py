from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task


# Create your views here.

def index(request):
    return HttpResponse("Index page")

def hello(request, username):
    print(type(username))
    return HttpResponse("<h1>Hello %s </h1>" % username)

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def task(request,tittle):
    task= get_object_or_404(Task, tittle=tittle)
    return HttpResponse("Task: %s" % task.tittle)