from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Task


# Create your views here.

def index(response, id):
    user = User.objects.get(id=id)
    return render(response, 'alltasks.html', {'user': user})

def landing_page(response):
    return render(response, 'index.html', {})