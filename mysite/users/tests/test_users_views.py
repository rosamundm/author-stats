from django.test import TestCase
from django.urls import reverse
from booksite import views
from users.models import CustomUser

# view in question: book_list
class TestSuccessView(TestCase):
    def anon_cannot_see_success_page(self):
        response = self.client.get(reverse("mybooks"))
        self.assertRedirects(
            response,
        )

    def auth_user_can_see_success_page(self):
        user = User.objects.create_user(
            "testview@email.com", "TestViewUser", "somepw123"
        )
        self.client.force_login(user=user)
        response = self.client.get(reverse("mybooks"))
        self.assertEqual(response.status_code, 200)


class TestLoginView(TestCase):
    def user_successfully_logged_in(self):
        response = self.client.get(reverse("login_success"))
