from django.db import models
from django.conf import settings
from django.urls import reverse

class User(models.Model):
    username = models.CharField(max_length=10, primary_key=True)  # ForeignKey ?
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=10)

    """
    user = User.objects.create_user("sample_username", "sample_email", "sample_pw")
    """

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=10, help_text="A working title is great!", null=True)
    synopsis = models.TextField(help_text="What's it about?", null=True)
    
    # change to CharField? :
    wordcount = models.IntegerField(help_text="Your word count when you added this title", null=True)
    goalwordcount = models.IntegerField(null=True)

    review = models.TextField(help_text="Any good so far?", null=True)


    def __str__(self):
        return self.title
