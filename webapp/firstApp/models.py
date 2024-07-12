<<<<<<< HEAD
=======

>>>>>>> 9a9893835dc918fb3fd0f8f92a8a5ffdee3e6b12
from django.db import models

# Create your models here.

class insurance(models.Model):
    age = models.FloatField()
    sex = models.FloatField()
    bmi = models.FloatField()
    children = models.FloatField()
    smoker = models.FloatField() 
    region = models.FloatField()
    expenses = models.FloatField()
