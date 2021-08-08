from .forms import CustomUserCreationForm, CustomLoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import CustomUser


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


def signup_success(request):
    return render(request, "registration/signup_success.html")


@login_required
def signin_success(request):
    return render(request, "registration/signin_success.html")


@login_required
def change_password(request):
    if request.method == 'POST':
        pw_change_form = PasswordChangeForm(request.user, request.POST)
        if pw_change_form.is_valid():
            user = pw_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed.')
            
            # see urls.py
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        pw_change_form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'pw_change_form': pw_change_form
    })


class CustomSignOutView(LogoutView):
    @login_required
    def signout(request):
        logout(request)
        return redirect("signin")


class ProfileView(TemplateView):
    def get(self, request, *args, **kwargs):
        user_id = self.request.user.id
        return render(request, "users/profile.html", {"user_id": user_id})
