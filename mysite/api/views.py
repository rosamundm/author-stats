from mybooks.models import Book
from .serializers import BookSerializer
from rest_framework import permissions, generics, viewsets
from rest_framework.response import Response
from django.shortcuts import render
import json


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("-date_added")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
