from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Task
from .forms import CreateNewTask

# Create your views here.

def all_tasks(response, id):
    user = User.objects.get(id=id)
    if response.method == "POST":
        for task in user.task_set.all():
            if response.POST.get("click" + str(task.id)) == "clicked":
                task.completed = True
            else:
                task.completed = False
            task.save()

    return render(response, 'alltasks.html', {'user': user})

def landing_page(response):
    return render(response, 'index.html', {})

def createtask(response):
    if response.method == "POST":
        form = CreateNewTask(response.POST)
        if form.is_valid():
            task = Task(user=User.objects.get(id=1), task_name=form.cleaned_data['task_name'], due_by=form.cleaned_data['due_by'], priority=form.cleaned_data['priority'], is_urgent=form.cleaned_data['is_urgent'])
            task.save()

        return HttpResponseRedirect("/%i" %1)
    
    form = CreateNewTask()
    return render(response, "createtask.html", {"form":form})