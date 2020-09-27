from django.test import TestCase
from mybooks.models import Book
from mybooks.forms import BookForm, BookDeleteForm


class TestAddBookForm(TestCase):
    def test_add_book(self):
        data = {
            "title": "some title",
            "synopsis": "some synopsis",
            "wordcount": 100,
            "goalwordcount": 1000,
            "review": "5 stars",
        }
        response = self.client.get("/mybooks/add/")
        self.assertTemplateUsed(response, "mybooks/create_book.html")
        self.assertContains(response, "title")
        self.assertContains(response, "synopsis")
        self.assertContains(response, "wordcount")
        self.assertContains(response, "goalwordcount")
        self.assertContains(response, "review")
        response = self.client.post("/mybooks/add", data=data)
        self.assertEqual(Book.objects.count(), 1)
        self.assertRedirects(response, "/mybooks/")


class TestDeleteBookForm(TestCase):
    def test_delete_book(self):
        pass
        # self.assertTemplateUsed(response, "mybooks/delete.html")
