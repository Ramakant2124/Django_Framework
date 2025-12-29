from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base_view, name=''),
    path('add/', views.add_course, name="add"),
    path('show/', views.show_course, name="show"),
    path('delete/<i>/', views.delete_course),
    path('update/<i>/', views.update_course),
]