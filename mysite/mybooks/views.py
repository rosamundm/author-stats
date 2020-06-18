from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserForm, BookForm
from .models import Book

# page views:

def index(request):
    return render(request, "mybooks/index.html")

def success(request):
    books = Book.objects.filter(date_added__lte=timezone.now()).order_by("date_added")
    return render(request, "mybooks/success.html", {"books": books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render (request, "mybooks/book_detail.html", {"book": book})

def create_book(request, pk):
    if request.method == "POST":
        # specify individual forms?
        createform = BookForm(request.POST)
        if createform.is_valid():
            book = createform.save(commit=False)
            book.date_added = timezone.now()
            book.save()
            return redirect("book_detail", pk=post.pk)
    else:
        createform = BookForm()
    return render(request, "mybooks/update.html", {"createform": createform})

def update_book(request):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        updateform = BookForm(request.POST, instance=book)
        if updateform.is_valid():
            book = updateform.save(commit=False)
            book.last_updated = timezone.now()
            book.save()
            return redirect("book_detail", pk=book.pk)
    else:
        updateform = BookForm(instance=book)
    return render(request, "mybooks/update.html", {"updateform": updateform})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("success")

def signup(request):
    return render(request, "mybooks/signup.html")

def about(request):
    return render(request, "mybooks/about.html")




# function views (should this be within index view?)

def get_username(request):
    if request.method == "POST":
        loginform = UserForm(request.POST)
        if loginform.is_valid():
            return HttpResponseRedirect("/success")
    else:
        loginform = UserForm()
    return render(request, "index.html", {"loginform": loginform})
