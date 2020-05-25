from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.shortcuts import render, get_object_or_404
from .forms import BookForm # to make


def book_list(request):
    #return HttpResponse("Welcome to my book collection!")
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "mybooks/book_list.html", context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {"book": book}
    return render(request, "mybooks/book_detail.html", context)

def new_book(request):
    context = {"form": form}
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author # form save??
            book.save()
            return redirect("book_detail", pk=book.pk)
    else: 
        form = BookForm
  #  return render(request, "mybooks/book_edit.html", context)

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {"form": form}
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author # form save??
            book.save()
            return redirect("book_detail", pk=book.pk)
    else:
        form = BookForm(instance=book)
  #  return render(request, "mybooks/book_edit.html", context)

def remove_book(request, ok):
    book = get_object_or_404(Book, pk=pk)
    book.delete() 
    return redirect("book_list")
