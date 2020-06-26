from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from .forms import BookForm #SignInForm, SignUpForm,
from .models import Book


def index(request):
    return render(request, "mybooks/index.html")
    if request.user.is_authenticated:
        return render(request, "mybooks/success.html")
"""
    # sign in as existing user:
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("success")
        else:
            signinform = SignInForm(request.POST)
            return render(request, "mybooks/success.html", {"signinform": signinform})
"""

def success(request):
    books = Book.objects.filter(date_added__lte=timezone.now()).order_by("date_added")
    return render(request, "mybooks/success.html", {"books": books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render (request, "mybooks/book_detail.html", {"book": book})

def create_book(request):
    if request.method == "POST":
        createform = BookForm(request.POST)
        if createform.is_valid():
            book = createform.save(commit=False)
            book.date_added = timezone.now()
            book.save()
            return redirect("/success/", pk=book.pk)
    else:
        createform = BookForm()
    return render(request, "mybooks/create_book.html", {"createform": createform})

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        updateform = BookForm(request.POST, instance=book)
        if updateform.is_valid():
            book = updateform.save(commit=False)
            book.last_updated = timezone.now()
            book.save()
            return redirect("/success/", pk=book.pk)
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

def contact_donate(request):
    return render(request, "mybooks/contact-donate.html")

def terms_conditions(request):
    return render(request, "mybooks/terms-conditions.html")



"""
# views for signing up and signing out:

def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        signupform = SignUpForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            username = signupform.cleaned_data.get("username")
            email = signupform.cleaned_data.get("email")
            password = signupform.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("success")
        else:
            return render(request, "mybooks/signup.html", {"signupform": signupform})
    else:
        signupform = SignUpForm()
        return render(request, "mybooks/signup.html", {"signupform": signupform})


def signin(request):
    if request.user.is_authenticated:
        return render(request, "mybooks/success.html")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("success")
        else:
            signinform = SignInForm(request.POST)
            return render(request, "mybooks/success.html", {"signinform": signinform})
    else:
        signinform = SignInForm()
        return render(request, "mybooks/index.html", {"signinform": signinform})


def signout(request):
    logout(request)
    return redirect("/")
"""
