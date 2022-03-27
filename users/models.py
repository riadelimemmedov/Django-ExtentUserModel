from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#!CustomUser Model
class CustomUser(AbstractUser):
    is_director = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=True)
    