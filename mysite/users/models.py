from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# defines what happens when user is created
class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        user = self.model(
           email = self.normalize_email(email),
           username = username,
           first_name = first_name,
           last_name = last_name,
           password = password
        )
        user.set_password(password)
        user.save(using=self.db)
        return user


# non-superuser model
class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=50,
        unique=True
        )
    username = models.CharField(
        max_length=20,
        unique=True
        )
    first_name = models.CharField(
        max_length=20,
        unique=False
        )
    last_name = models.CharField(
        max_length=20,
        unique=False
        )
    password = models.CharField(
        max_length=20,
        unique=False
        )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    objects = CustomAccountManager()


    def __str__(self):
        return self.username

"""
class NewsletterRecipient(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
"""
