from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
CHOICES = [("JS", "JobSeeker"), ("EMP", "Employer")]
class User(AbstractUser):
    position = models.CharField(max_length = 10, choices = CHOICES)