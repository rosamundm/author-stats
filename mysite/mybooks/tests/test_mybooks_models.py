from django.test import TestCase
from .models import Book
from datetime import datetime
from model_bakery import baker

# for pytest only:
import pytest
from django.urls import reverse


@login_required
class TestBookModel(TestCase):
    def test_book_model(self):
        # baker populates test object with data:
        book = baker.make("mybooks.Book")
        assert book.title
        print(book.__dict__)
