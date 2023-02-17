from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home")
    path("hello/", views.home, name="home")
    path("contact/", views.home, name="home")
    path("aboutus/", views.home, name="home")
]
