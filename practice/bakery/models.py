from django.db import models

# Create your models here.

class Cake(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    created_on=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name+"("+str(self.price)+")"


class Biscuit(models.Model):
    name=models.CharField(max_length=30)
    flavour=models.CharField(choices=(("sweet","sweet"),("salty","salty"),("cream","cream")),max_length=30)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    created_on=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name+"("+str(self.price)+")"