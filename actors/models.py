from django.db import models

# Create your models here.

#!Actor Model
class Actor(models.Model):
    name = models.CharField(max_length=200)
    is_star = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.name)