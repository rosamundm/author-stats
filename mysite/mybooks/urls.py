from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"), #index 
]

