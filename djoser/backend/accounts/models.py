from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy
from django.utils import timezone
# Create your models here.

class CustomUser(BaseUserManager):
    def create_superuser(self,user_name, email, phone, password,**other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        
        return self.create_user(user_name, email, phone, password, **other_fields)
    
    
        
        
    def create_user(self, user_name, email, phone, password=None, **other_fields):
        if not email:
            raise ValueError(gettext_lazy('Email is required'))
        other_fields.setdefault('is_active', True)
        email = self.normalize_email(email)
        user = self.model(user_name=user_name, email=email, phone=phone, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserAccount(AbstractBaseUser,PermissionsMixin):
    user_name = models.CharField(unique=True, max_length=255)
    email = models.EmailField(gettext_lazy('email address'), unique=True)
    phone = models.CharField(max_length=30)
    register_date = models.DateTimeField(default=timezone.now)
    is_varified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUser()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone','user_name']
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
