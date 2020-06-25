from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
#from statistics.wordcounts import ___

class Book(models.Model):
    date_added = models.DateTimeField(
                    default=timezone.now,
                    null=True)
    title = models.CharField(
                    max_length=50,
                    help_text="A working title is great!",
                    null=True)
    synopsis = models.TextField(
                    help_text="What's it about?",
                    null=True)
    wordcount = models.IntegerField(
                    help_text="Your current word count",
                    null=True,
                    verbose_name="Word count")
    goalwordcount = models.IntegerField(
                    help_text="What are you aiming for?",
                    null=True,
                    verbose_name="Goal word count")
    review = models.TextField(
                    help_text="Add any extra notes here",
                    null=True)

    def __str__(self):
        return self.title

    def update_book(self):
        pass



    def rolling_wordcount(self):
        pass

"""
# list of accumulated words added, for monthly average:
date_recorded = ["2020-06-22", "2020-06-23", "2020-06-24"]
word_difference = [343, 12, 1000]
zipped = zip(date_recorded, word_difference)
words_with_dates = {key: value for key, value in zipped}
"""
