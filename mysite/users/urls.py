from django.contrib import admin
from django.urls import include, path
from .views import CustomSignOutView, ProfileView
from . import views

urlpatterns = [
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path("signout/", CustomSignOutView.as_view(), name="signout"),
    
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signup_success/", views.signup_success, name="signup_success"),
    path("signin_success/", views.signin_success, name="signin_success"),

    path("change_password/", views.change_password, name='change_password'),

]
