from mybooks.models import Book
from mybooks.serializers import BookSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("-date_added")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class HelloView(APIView):
    def get(self, request):
        content = {"message": "Hello world!"}
        return Response(content)
