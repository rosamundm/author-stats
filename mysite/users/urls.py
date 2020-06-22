from django.contrib import admin
from django.urls import include, path
from . import views

"""
urlpatterns = [
    path("signin/", SignInView.as_view(), name="signin"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
"""

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
]
