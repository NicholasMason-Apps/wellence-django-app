from django.shortcuts import redirect, render
from .models import Task
from .forms import CreateNewTask
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px

# Create your views here.

@login_required
def all_tasks(response):
    user = response.user
    if response.method == "POST":
        for task in user.tasks.all():
            if response.POST.get("delete" + str(task.id)) == "clicked":
                task.delete()
                continue
            elif response.POST.get("click" + str(task.id)) == "clicked":
                task.completed = True
            else:
                task.completed = False
            task.save()
        messages.add_message(response, messages.INFO, "Successfully saved changes")
        return redirect('all_tasks')
    
    df = pd.DataFrame(user.tasks.all().values())
    df_under_30_days = df[df['due_by'] <= str(datetime.now() + timedelta(days=30))]
    df_under_30_days = pd.DataFrame(dict(x = df['due_by'], y = df['task_name']))
    lc_fig = px.line(df_under_30_days, x="x", y="y", title="Tasks due within 30 Days", labels={
        'x': 'Due By (hh:mm yyyy-mm-dd)',
        'y': 'Task Name'
    })
    pcfig = px.pie() # To add
    return render(response, 'alltasks.html', {'user': user, 'line_chart':lc_fig.to_html(full_html=False)})

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
        return redirect('createtask')
    
    form = CreateNewTask()
    return render(response, "createtask.html", {"form":form, 'user':response.user})
