from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class NewsletterRecipient(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
