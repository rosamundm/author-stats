from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

class Book(models.Model):
    date_added = models.DateTimeField(
                    default=timezone.now,
                    null=True)
    last_updated = models.DateTimeField(
                    auto_now=True,
                    null=True)
    title = models.CharField(
                    max_length=50,
                #    help_text="A working title is great!",
                    null=True)
    synopsis = models.TextField(
                #    help_text="What's it about?",
                    null=True)
    wordcount = models.IntegerField(
                #    help_text="Your current word count",
                    null=True,
                    verbose_name="Word count")
    goalwordcount = models.IntegerField(
                #    help_text="What are you aiming for?",
                    null=True,
                    verbose_name="Goal word count")
    review = models.TextField(
                #    help_text="Add any extra notes here",
                    null=True)

    def __str__(self):
        return self.title

    # words remaining until goal is reached:
    def words_remaining(self):
        remaining = self.goalwordcount-self.wordcount
        return remaining

    # words remaining as a percentage:
    def words_remaining_pc(self):
        words_by_100 = self.wordcount * 100
        remaining_pc = words_by_100 / self.goalwordcount
        return remaining_pc

    # words written since last time:
    def words_added(wordcount, added):
        if wordcount and added:
            wordcount += added
        return wordcount

    # words edited out since last time:
    def words_deleted(wordcount, deleted):
        if wordcount and deleted:
            wordcount -= deleted
        return wordcount







"""
# list of accumulated words added, for monthly average:
date_recorded = ["2020-06-22", "2020-06-23", "2020-06-24"]
word_difference = [343, 12, 1000]
zipped = zip(date_recorded, word_difference)
words_with_dates = {key: value for key, value in zipped}


# to do:
# avg words written per day/week/month:
def words_per_day(wordcount, goalwordcount):
    pass # make this returnable in views

    # use Pandas to find average per day!

    PSEUDOCODE:

    Book.wordcount.get.all()
    -> put these into a list


    for w in list:
        [add them up together]
        [save to a new variable]
        [show variable in template] <--- should have name like "wordsinweek", "wordsinday"


Book.objects.values_list("wordcount")




    """
