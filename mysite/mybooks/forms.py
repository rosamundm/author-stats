from django import forms
from django.core.exceptions import ValidationError
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "synopsis",
            "wordcount",
            "goalwordcount",
            "review"
            ]
