import datetime
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from users.models import CustomUser
from simple_history.models import HistoricalRecords


class Book(models.Model):
    author = models.ForeignKey(
        null=True,
        blank=False,
        related_name="books",
        on_delete=models.CASCADE,
        to=CustomUser,
    )
    date_added = models.DateTimeField(default=timezone.now, null=True)
    last_updated = models.DateTimeField(auto_now=True, db_index=True, null=True)
    title = models.CharField(
        max_length=50, help_text="A working title is great!", null=True
    )
    synopsis = models.TextField(help_text="What's it about?", null=True)
    wordcount = models.IntegerField(
        help_text="Your current word count", null=True, verbose_name="Word count"
    )
    goalwordcount = models.IntegerField(
        help_text="What are you aiming for?", null=True, verbose_name="Goal word count"
    )
    review = models.TextField(help_text="Add any extra notes here", null=True)

    # for django-simple-history:
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    # words remaining until goal is reached:
    def words_remaining(self):
        remaining = self.goalwordcount - self.wordcount
        return remaining

    # words remaining as a percentage:
    def words_remaining_pc(self):
        words_by_100 = self.wordcount * 100
        remaining_pc = words_by_100 / self.goalwordcount
        if remaining_pc < 1:
            return round(remaining_pc, 1)
        else:
            return round(remaining_pc)
