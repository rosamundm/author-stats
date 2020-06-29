from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.edit import CreateView, FormView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    signupform = CustomUserCreationForm(data=request.POST)
    if request.method == "POST":
        if signupform.is_valid():
            signupform.save()
            return redirect("/user/signin")
        else:
            signupform = CustomUserCreationForm()
        return render(request, "registration/signup.html", {"signupform": signupform})


def signin(request):
    signinform = CustomLoginForm(data=request.POST)
    if request.method == "POST":
        if signinform.is_valid():
            username = signinformform.cleaned_data["username"]
            password = signinformform.cleaned_data["password"]
            user = authenticate(request, username=username, password= password)
            if user is not None:
                login(request, user)
                return render(redirect, "mybooks/success.html")
            else:
                return render(redirect, "mybooks/nosuccess.html")
        else:
            return render(redirect, "registration/signin.html", {"signinform": signinform})
    else:
        return render(redirect, "registration/signin.html", {"signinform": signinform})
