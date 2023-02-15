from django.db import models

# Create your models here.
class Car(models.Model):
    Name = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Cost = models.CharField(max_length=100)
    Color = models.CharField(max_length=50)
    Top_Speed = models.CharField(max_length=100)