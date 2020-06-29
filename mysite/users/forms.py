from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser, NewsletterRecipient

class CustomLoginForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "password",
            ]

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            ]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            ]

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterRecipient
        fields = [
            "name",
            "email",
        ]
