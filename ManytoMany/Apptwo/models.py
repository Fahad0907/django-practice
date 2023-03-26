from django.db import models

# Create your models here.
class A(models.Model):
    name = models.CharField(max_length=255)
    intt = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name

class B(models.Model):
    name = models.CharField(max_length=255)
    intt = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class C(models.Model):
    a_id = models.ForeignKey(A,on_delete=models.CASCADE)
    b_id = models.ForeignKey(B,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
    
    
#TRIED NESTED API
class Phone(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

class PhoneUser(models.Model):
    name = models.CharField(max_length=255)
    age = models.SmallIntegerField()
    phone_id = models.ForeignKey(Phone,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    p_user = models.ForeignKey(PhoneUser,on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name