from django import forms
from django.core.exceptions import ValidationError
from .models import Book

"""
class SignInForm(forms.ModelForm):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=10)
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]
"""

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "date_added",
            "title",
            "synopsis",
            "review"
            ]
