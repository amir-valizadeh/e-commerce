
from itertools import product
from django.db import models


# Create your models here.
class Product(models.Model):
    
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True,default='/images/default.jpg',upload_to='images/')
    category = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    createdAt=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name +" - "+ self.category
    