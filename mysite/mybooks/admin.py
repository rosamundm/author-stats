from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Book
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Book, SimpleHistoryAdmin)


class BookAdmin(ModelAdmin):
    # add proper "icontains" queries here...
    search_fields = ["title", "synopsis", "review"]
