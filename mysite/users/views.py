from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.edit import CreateView, FormView
from .forms import NewsletterForm
from .models import NewsletterRecipient
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    #signupform = CustomUserCreationForm(data=request.POST)

    if request.method == "POST":
        newsform = NewsletterForm(request.POST)
        if newsform.is_valid():
            n = newsform.save(commit=False)
            if NewsletterRecipient.objects.filter(email=n.email).exists():
                return HttpResponse(str("That email address is already in use"))
            else:
                n.save()
                return HttpResponse(str("Thanks for signing up"))
    else:
        newsform = NewsletterForm()
    return render(request, "registration/signup.html", {"newsform": newsform})








def signin(request):
    #signinform = CustomLoginForm(data=request.POST)

    if request.method == "POST":
        newsform = NewsletterForm(request.POST)
        if newsform.is_valid():
            n = newsform.save()
            return "Thank you for signing up!"
    else:
        newsform = NewsletterForm()
    return render(redirect, "registration/signin.html", {"newsform": newsform})
