from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField()
    
    def __str__(self) -> str:
        return f"{self.name} -- {str(self.price)}"
    
class Bucket(models.Model):
    name = models.CharField(max_length=500)
    total_price = models.FloatField(default=0)
    car_list = models.ManyToManyField(Car)
    
    def __str__(self) -> str:
        return self.name