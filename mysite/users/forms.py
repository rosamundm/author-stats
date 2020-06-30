from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser#, NewsletterRecipient

# form for registration
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1", # new
            "password2" # new
            ]


class CustomLoginForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password",
            ]

    # verify user's credentials
    def clean(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid details")





class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            ]

"""
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterRecipient
        fields = [
            "name",
            "email",
        ]
"""
