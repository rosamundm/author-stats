from django.test import TestCase
from users.models import CustomUser
from users.forms import CustomUserCreationForm, CustomLoginForm, CustomUserChangeForm


class TestCustomUserCreationForm(TestCase):
    def test_register_user(self):
        data = {
            "username": "some_username",
            "first_name": "salt",
            "last_name": "pepper",
            "email": "email@email.com",
            "password1": "v3rysecurepassw0rd",
            "password2": "v3rysecurepassw0rd",
        }
        # test POST requests:
        response = self.client.post("/signup/", data=data)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertRedirects(response, "/signin/")
        self.assertTemplateUsed(response, "registration/signup.html")


class TestCustomLoginForm(TestCase):
    def test_login_user(self):
        pass
        # self.assertTemplateUsed(response, "registration/signin.html")


class TestCustomUserChangeForm(TestCase):
    def test_change_user(self):
        pass
