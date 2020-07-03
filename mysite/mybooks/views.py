from django.utils import timezone
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookForm#, BookDeleteForm
from .models import Book

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

def index(request):
    return render(request, "mybooks/index.html")
    if request.user.is_authenticated:
        return render(request, "mybooks/mybooks.html")

@login_required
def book_list(request): # aka "success"
    books = Book.objects.filter(date_added__lte=timezone.now()).order_by("date_added")
    return render(request, "mybooks/book_list.html", {"books": books})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render (request, "mybooks/book_detail.html", {"book": book})

@login_required
def create_book(request):
    if request.method == "POST":
        createform = BookForm(request.POST)
        if createform.is_valid():
            book = createform.save(commit=False)
            book.date_added = timezone.now()
            book.save()
            return redirect("/mybooks/", pk=book.pk)
    else:
        createform = BookForm()
    return render(request, "mybooks/create_book.html", {"createform": createform})

@login_required
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        updateform = BookForm(request.POST, instance=book)
        if updateform.is_valid():
            book = updateform.save(commit=False)
            book.last_updated = timezone.now()
            book.save()
            return redirect("/mybooks/", pk=book.pk)
    else:
        updateform = BookForm(instance=book)
    return render(request, "mybooks/update.html", {"updateform": updateform})


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted!")
        return redirect("/mybooks")
    return render(request, "mybooks/delete.html", {"book": book})

def signup(request):
    return render(request, "mybooks/signup.html")

def about(request):
    return render(request, "mybooks/about.html")

def contact(request):
    return render(request, "mybooks/contact.html")

def terms_conditions(request):
    return render(request, "mybooks/terms-conditions.html")

@login_required
def stats(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render (request, "mybooks/stats.html", {"book": book})
