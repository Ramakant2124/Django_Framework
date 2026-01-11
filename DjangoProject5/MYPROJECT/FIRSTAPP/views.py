from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LaptopModelForm
from .models import LaptopModel
from django.core.mail import send_mail

# Create your views here.
def home_page_view(request):
    template_name = 'FIRSTAPP/home.html'
    context = {}
    return render(request, template_name, context)

def show_laptops_view(request):
    laptop_objs_qs = LaptopModel.objects.all()
    template_name = 'FIRSTAPP/show_laptops.html'
    context = {"laptop_objs_qs":laptop_objs_qs}
    return render(request, template_name, context)

def add_laptops_view(request):
    form = LaptopModelForm()
    if request.method == "POST":
        form = LaptopModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("show")
    template_name = 'FIRSTAPP/add_laptops.html'
    context = {"form":form}
    return render(request, template_name, context)

def test_send_email_view(request):
    print("Sending email Started......")
    send_mail(
        "subject:Test Subject",
        "message:Text Msg body",
        "chaudhari2124@gmail.ccom",
        ["ramakantchaudhari9834@gmail.com"],
        fail_silently=False,
        )
    print("Mail send......")
    return HttpResponse("Mail sent.")
