from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user = models.PositiveIntegerField(null=True, blank=True)
