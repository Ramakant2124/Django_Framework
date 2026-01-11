from tempfile import template

from django.contrib.auth import authenticate ,login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created, you can now login",extra_tags="alert alert-success")
            return redirect("login")
    template_name = "AUTHAPP/register.html"
    context = {"form": form}
    return render(request, template_name, context)

def login_view(request):
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["password"]
        user= authenticate(request,username=u, password=p)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password",extra_tags="danger")
    template_name = "AUTHAPP/login.html"
    context = {}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect("login")