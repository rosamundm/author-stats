from django.contrib import admin
from django.urls import include, path
from .views import SignUpView #SignInView

urlpatterns = [
#    path("signin/", SignInView.as_view(), name="signin"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
