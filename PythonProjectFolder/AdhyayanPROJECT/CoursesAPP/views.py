from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CourseModelForm
from .models import CourseModel
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CourseModel


# Create your views here.
def show_courses_view(request):
    template_name = 'CoursesAPP/show_courses.html'
    courses_objs_qs = CourseModel.objects.all()
    context = {"courses_objs_qs": courses_objs_qs}
    return render(request, template_name, context)

def add_courses_view(request):
    if request.method == "GET":
        template_name = 'CoursesAPP/add_courses.html'
        form = CourseModelForm()
        context = {"form": form}
        return render(request, template_name, context)
    elif request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show")
        else:
            return HttpResponse("Couese Added Successfully")

def delete_courses_view(request,i):
     course_obj = CourseModel.objects.get(id=i)
     course_obj.delete()
     return redirect("show")

def update_courses_view(request,i):
    course_obj = CourseModel.objects.get(id=i)
    form = CourseModelForm(instance=course_obj)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course_obj)
        if form.is_valid():
            form.save()
            return redirect("show")
    template_name = 'CoursesAPP/add_courses.html'
    context = {"form": form}
    return render(request, template_name, context)
