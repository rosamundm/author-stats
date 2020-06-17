from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserForm

# page views:

def index(request):
    return render(request, "mybooks/index.html")

def success(request):
    return render(request, "mybooks/success.html")

def signup(request):
    return render(request, "mybooks/signup.html")

def about(request):
    return render(request, "mybooks/about.html")

def update(request):
    return render(request, "mybooks/update.html")


# function views (should this be within index view?)

def get_username(request):
    if request.method == "POST":
        loginform = UserForm(request.POST)
        if loginform.is_valid():
            return HttpResponseRedirect("/success")
    else:
        loginform = UserForm()
    return render(request, "index.html", {"loginform": loginform})
