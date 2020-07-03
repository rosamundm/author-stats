from django.test import TestCase
import views.py


class TestSuite(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email = "user@blah.com",
            username = "some_user",
            password = "secret_pw123"
        )

    def create_user_test(self):
        response = self.client.post(
            "/login",
            {"email": "user@blah.com",
             "username": "some_user",
             "password": "password"
            } 
        )
