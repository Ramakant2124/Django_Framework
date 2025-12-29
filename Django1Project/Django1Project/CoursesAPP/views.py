from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def python_course_view(request):
     return HttpResponse(" Hello from python course view")
