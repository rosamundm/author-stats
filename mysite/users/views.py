from django.views.generic.edit import CreateView, FormView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

"""
class SignInView(≈≈≈):
    form_class = CustomLoginForm
    template_name = "registration/signin.html"
    success_url = "/success/"
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = "/success/"
"""


def signup(request):
        if request.method == "POST":
            form = CustomUserCreationForm(data=request.POST)
            if form.is_valid():
                form.save()
            return redirect("/user/login")
        else:
            form = CustomUserCreationForm()

        return render(request, "registration/signup.html", {"form": form})

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/success")
    else:
        form = CustomLoginForm()

    return render(request, "registration/signin.html", {"form": form})
