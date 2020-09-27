from .forms import CustomUserCreationForm, CustomLoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.contrib.auth.decorators import login_required
from django.views import generic


def signup(request):
    signupform = CustomUserCreationForm(data=request.POST)
    if request.method == "POST":
        if signupform.is_valid():
            signupform.save()
            user = signupform.cleaned_data.get("username", "password")
            return HttpResponseRedirect(reverse("signup_success"))
    return render(request, "registration/signup.html", {"signupform": signupform})


def signin(request):
    signinform = CustomLoginForm(data=request.POST)
    if request.method == "POST":
        if signinform.is_valid():
            username = signinform.cleaned_data.get("username")
            password = signinform.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("signin_success"))
            else:
                return HttpResponse("Your account is not active")
        else:
            return HttpResponse("Incorrect details")
    else:
        return render(request, "registration/signin.html", {"signinform": signinform})


class CustomSignOutView(LogoutView):
    @login_required
    def signout(request):
        logout(request)
        return redirect("signin")

def signup_success(request):
    return render(request, "registration/signup_success.html")

@login_required
def signin_success(request):
    return render(request, "registration/signin_success.html")
