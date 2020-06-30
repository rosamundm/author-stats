from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.edit import CreateView, FormView
from .forms import CustomUserCreationForm, CustomLoginForm #NewsletterForm
#from .models import NewsletterRecipient
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    context = {}
    if request.method == "POST":
        signupform = CustomUserCreationForm(data=request.POST)
        if signupform.is_valid():
            signupform.save()
            email = signupform.cleaned_data.get("signupform")
            raw_password = signupform.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect("/success/")
        else:
            context["signupform"] = signupform
    else:
        signupform = CustomUserCreationForm
    return render(request, "registration/signup.html", context)


def signin(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("/about")
    elif request.method == "POST":
        signinform = CustomLoginForm(data=request.POST)
        if signinform.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("/success")
    else:
        signinform = CustomLoginForm()
    context["signinform"] = signinform
    return render(request, "registration/signin.html", context)





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
