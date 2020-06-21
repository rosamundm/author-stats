from django.contrib import admin
from django.urls import include, path
from . import views

# list these in same order as views for elegance!
urlpatterns = [
     path("", views.index, name="index"),
#     path("signin/", views.signin, name="signin"),
#     path("signup/", views.signup, name="signup"),
     path("success/", views.success, name="success"),
     path("mybooks/<int:pk>/", views.book_detail, name="book_detail"),
     path("mybooks/<int:pk>/update/", views.update_book, name="update"),
     path("mybooks/<pk>/delete/", views.delete_book, name="delete"),
     path("about/", views.about, name="about"),
]
