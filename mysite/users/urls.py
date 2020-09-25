from django.contrib import admin
from django.urls import include, path
from .views import CustomSignOutView
from . import views

urlpatterns = [

    path(
        "signup/",
        views.signup,
        name="signup"
        ),

    path(
        "signin/",
        views.signin,
        name="signin"
        ),

    # this actually works — keep!
    path(
        "signout/",
        CustomSignOutView.as_view(),
        name="signout"
        ),

    path(
        "account_created/",
        views.account_created,
        name="account_created"
    ),

    path(
        "login_success/",
        views.login_success,
        name="login_success"
    )

]
