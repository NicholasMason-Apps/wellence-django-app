from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Task


# Create your views here.

def index(response, id):
    user = User.objects.get(id=id)
    task = user.task_set.get(id=1)
    return HttpResponse('<h1>%s</h1><br><p>%s</p>' %(user.email, task.task_name))

def landing_page(response):
    return HttpResponse('Home')