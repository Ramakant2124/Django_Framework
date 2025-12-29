from  django.urls import path
from . import views


urlpatterns = [
    path("show/", views.show_courses_view, name="show"),
    path("add/", views.add_courses_view, name="add"),
    path("delete/<i>/", views.delete_courses_view),
    path("update/<i>/", views.update_courses_view),

]