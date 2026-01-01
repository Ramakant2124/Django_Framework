from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["password"]
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect("show")
        else:
            return redirect("login")
    template_name = 'AuthAPP/login.html'
    context = {}
    return render(request, template_name, context)






def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'AuthAPP/register.html'
    context = {'form': form}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect("login")