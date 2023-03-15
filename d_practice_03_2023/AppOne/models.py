from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class CustomerUser(BaseUserManager):
    def create_superuser(self,email,password=None,**other_fields):
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_staff',True)
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_staff') is not True:
            raise ValueError('staff must be assigned to is_superuser=True')
        return self.create_user(email,password,**other_fields)
    
    def create_user(self,email,password=None,**other_fields):
        if not email:
            raise ValueError('email is required')
        other_fields.setdefault('is_active',True)
        email = self.normalize_email(email)
        user = self.model(email=email,**other_fields)
        user.set_password(password)
        user.save()
        return user
        
class User(AbstractBaseUser):
    user_code = models.CharField(max_length=255,blank=True)
    username = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomerUser()
    # def save(self, *args,**kwargs):
    #     if self.user_code == "":
    #         self.user_code = "A5896"
    #     return super().save(*args,**kwargs)
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def get_username(self) -> str:
        return self.username
    
    def get_full_name(self) -> str:
        return self.first_name + " " + self.last_name
    

class AnotherTable(models.Model):
    userr = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=500)
    
class Blog(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True,blank=True)
    
    
class Customer(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.name} - {self.age}"

class Product(models.Model):
    amount = models.FloatField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.customer.name} - {self.amount}"