from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "date_added",
            "wordcount",
            "goalwordcount",
        ]
