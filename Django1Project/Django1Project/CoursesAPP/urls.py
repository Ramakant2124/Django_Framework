from Django1Project.Django1Project.urls import urlpatterns
from django.urls import path
from .views import python_course_view


urlpatterns =[
    path("python/",python_course_view)
]