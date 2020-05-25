from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    date_finished = models.DateField(blank=True, null=True)
    review = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
 


