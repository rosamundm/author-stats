from django import forms
from django.core.exceptions import ValidationError
from .models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget = forms.PasswordInput())
