from django.db import models

# Create your models here.
class yahoo(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.CharField(max_length=255)
    date = models.DateField()
    Open = models.FloatField(null=True,blank=True)
    High = models.FloatField(null=True,blank=True)
    Low = models.FloatField(null=True,blank=True)
    Close = models.FloatField(null=True,blank=True)
    Volume = models.FloatField(null=True,blank=True)
    Dividends = models.FloatField(null=True,blank=True)
    StockSplits = models.FloatField(null=True,blank=True)
    class Meta:
        indexes = [models.Index(fields=['ticker','date'])]
    
class T(models.Model):
    name =  models.CharField(max_length=255)
    
class Tryindex(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    
    class Meta:
        indexes = [models.Index(fields=['name','email'])]