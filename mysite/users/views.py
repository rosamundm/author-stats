from django.views.generic.edit import CreateView, FormView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.shortcuts import render, redirect

"""
class SignInView(FormView):
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
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("/user/login")
        else:
            form = CustomUserCreationForm()

        return render(request, "registration/signup.html", {"form": form})

def signin(request):
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/success")
    else:
        form = CustomLoginForm()

    return render(request, "registration/signin.html", {"form": form})
