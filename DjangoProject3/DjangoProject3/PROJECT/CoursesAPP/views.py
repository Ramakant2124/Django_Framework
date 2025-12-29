from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course

# Create your views here.
def base_view(request):
    template_name = 'base.html'
    context = {}
    return render(request, template_name, context)

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course Added successfully!")
            return redirect('show')
    template_name = 'CoursesAPP/add_courses.html'
    course_form = CourseForm()
    context = {"course_form": course_form}
    return render(request, template_name, context)

def show_course(request):
    template_name = 'CoursesAPP/show_courses.html'
    course_obj = Course.objects.all()
    context = {"course_obj": course_obj}
    return render(request, template_name, context)

def delete_course(request,i):
    obj = Course.objects.get(id=i)
    obj.delete()
    messages.success(request, "Course deleted successfully!")
    return redirect('show')

def update_course(request,i):
    course_obj = Course.objects.get(id=i)
    form = CourseForm(instance=course_obj)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('show')
    template_name = 'CoursesAPP/add_courses.html'
    context = {"course_form": form}
    return render(request, template_name, context)
