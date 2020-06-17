from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Book
from django.shortcuts import render, get_object_or_404
from .forms import BookForm
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import loader

def index(request):
    return render(request, "mybooks/base.html")

def signup(request):
    return render(request, "mybooks/signup.html")

def about(request):
    return render(request, "mybooks/about.html")

def update(request):
    return render(request, "mybooks/update.html")
