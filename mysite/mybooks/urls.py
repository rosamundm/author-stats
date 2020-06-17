from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
     path("", views.index, name="index"),
     path("signup/", views.signup, name="signup"),
     path("about/", views.about, name="about"),
     path("success/", views.success, name="success")
]
