from django.db import models
from django.conf import settings
from django.urls import reverse

class User(models.Model):
    username = models.CharField(max_length=10, primary_key=True)  # ForeignKey ?
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=10)




    def __str__(self):
        return self.username




class Book(models.Model):
    title = models.CharField(max_length=10, help_text="A working title is great!", null=True)
    # ForeignKey: many-to-one, i.e. author can have several books
    # null=True: database can store null value if no author selected
    # on_delete=models.SET_NULL: when deleted, author value set to null
    synopsis = models.TextField(help_text="What's it about?", null=True)
    wordcount = models.IntegerField(help_text="Your word count when you added this title", null=True)
    #to do! rating
    review = models.TextField(help_text="Any good so far?", null=True)


    def __str__(self):
        return self.title
