from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.edit import CreateView, FormView
from .forms import CustomUserCreationForm, CustomLoginForm #NewsletterForm
#from .models import NewsletterRecipient
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    signupform = CustomUserCreationForm(data=request.POST)
    if request.method == "POST":
        if signupform.is_valid():
            signupform.save()
            user = signupform.cleaned_data.get("username")
            messages.success(request, "Account created")
            return redirect("signin")
    if request.user.is_authenticated:
        return redirect("success")
    return render(request, "registration/signup.html", {"signupform": signupform})


def signin(request):
    signinform = CustomLoginForm(data=request.POST)
    if request.method == "POST":
        if signinform.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return render(request, "mybooks/success.html", context)
    elif request.user.is_authenticated:
        return redirect("success")
    else:
        messages.info(request, "Details incorrect")
    return render(request, "registration/signin.html", {"signinform": signinform})


def signout(request):
    logout(request)
    return redirect("signin")



"""
    #### NEWSLETTER ####
    if request.method == "POST":
        newsform = NewsletterForm(request.POST)
        if newsform.is_valid():
            n = newsform.save(commit=False)
            if NewsletterRecipient.objects.filter(email=n.email).exists():
                return render(request, "registration/newsletter_success.html")
                #return HttpResponse(str("That email address is already in use"))
            else:
                n.save()
                #return HttpResponse(str("Thanks for signing up"))
                return render(request, "registration/newsletter_success.html")
    else:
        newsform = NewsletterForm()
    return render(request, "registration/signup.html", {"newsform": newsform})
"""
