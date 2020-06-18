from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


class User(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, on_delete=models.CASCADE)  # ForeignKey ?
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class Book(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50, help_text="A working title is great!", null=True)
    synopsis = models.TextField(help_text="What's it about?", null=True)

    # change to CharField? :
    wordcount = models.IntegerField(help_text="Your word count when you added this title", null=True)
    goalwordcount = models.IntegerField(null=True)

    review = models.TextField(help_text="Any good so far?", null=True)


    def __str__(self):
        return self.title
