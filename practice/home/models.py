from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class MovieRelease(models.Model):
    title= models.CharField(max_length=50)
    studio=models.CharField(max_length=40)
    release_date=models.DateTimeField()

