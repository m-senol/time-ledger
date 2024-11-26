from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import LEAVE_DAYS

# Create your models here.

class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    hire_date = models.DateField(null=True, blank=True)
    available_leave_days = models.IntegerField(default=LEAVE_DAYS)

    def __str__(self):
        return self.username
