from django.db import models
from actors.models import *

# Create your models here.

#!Movie Model
class Movie(models.Model):
    title = models.CharField(max_length=200)
    actors = models.ManyToManyField(Actor,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

#!Film Model
class Film(Movie):
    length = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.title)
    
#!Commercial Model
class Commercial(Movie):
    company = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.title)