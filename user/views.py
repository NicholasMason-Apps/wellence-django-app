from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/")


    form = RegisterForm()
    return render(response, "register.html", {"form":form})