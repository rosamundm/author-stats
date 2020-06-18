from django import forms
from django.core.exceptions import ValidationError
from .models import User, Book

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget = forms.PasswordInput())


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "date_added",
            "title",
            "synopsis",
            "review"
            ]
