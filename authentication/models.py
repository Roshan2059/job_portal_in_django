from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
CHOICES = [("JS", "jobseeker"), ("EMP", "employer")]
class User(AbstractUser):
    position = models.CharField(max_length = 10, choices = CHOICES)