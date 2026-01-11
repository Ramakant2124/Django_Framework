from  django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page_view, name='home'),
    path('show/', views.show_laptops_view, name='show'),
    path('add/', views.add_laptops_view, name='add'),
    path('test/', views.test_send_email_view, name='test'),
]