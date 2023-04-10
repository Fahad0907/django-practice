from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    age = models.SmallIntegerField()
    
    def __str__(self) -> str:
        return str(self.name)