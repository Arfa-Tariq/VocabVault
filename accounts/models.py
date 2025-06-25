from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # Add custom fields later (e.g., language_level, XP, etc.)
    pass