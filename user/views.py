from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def register(response):
    # Very simple register form which leverages the built-in login system in Django.
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            messages.error(response, form.errors)
            return redirect('register')

    form = RegisterForm()
    return render(response, "register.html", {"form":form})

def logout_view(response):
    logout(response)
    return redirect('landing_page')