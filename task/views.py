from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from .forms import CreateNewTask
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def all_tasks(response):
    user = response.user
    if response.method == "POST":
        for task in user.task_set.all():
            if response.POST.get("click" + str(task.id)) == "clicked":
                task.completed = True
            else:
                task.completed = False
            task.save()
        messages.add_message(response, messages.INFO, "Successfully saved changes")
    return render(response, 'alltasks.html', {'user': user})

def landing_page(response):
    return render(response, 'index.html', {'user':response.user})

@login_required
def createtask(response):
    if response.method == "POST":
        form = CreateNewTask(response.POST)
        if form.is_valid():
            task = Task(task_name=form.cleaned_data['task_name'], due_by=form.cleaned_data['due_by'], priority=form.cleaned_data['priority'], is_urgent=form.cleaned_data['is_urgent'])
            task.save()
            response.user.tasks.add(task)
            messages.add_message(response, messages.INFO, "Task successfully created")
        else:
            messages.add_message(response, messages.INFO, "Task Creation Failed")
    
    form = CreateNewTask()
    return render(response, "createtask.html", {"form":form, 'user':response.user})
