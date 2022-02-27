from email import charset, message
import email
from django.db import models
from django.forms import CharField, IntegerField

class StudentInfo(models.Model):
    name=models.CharField(max_length=45)
    standard=models.IntegerField()
    dob=models.DateField()
    totalMarks=models.FloatField()

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name=models.CharField(max_length=50)
    of=models.ForeignKey(StudentInfo,on_delete=models.CASCADE)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    message=models.TextField()

    def __str__(self):
        return self.name