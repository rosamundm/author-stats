from mybooks.models import Book
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "date_added",
            "wordcount",
            "goalwordcount",
        ]
