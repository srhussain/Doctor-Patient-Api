from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager



    
# Create your models here.

class User(AbstractUser):
    username=models.CharField(max_length=20,unique=True)
    email=models.EmailField(unique=True)
    profile=models.ImageField(null=True,blank=True)
    is_patient=models.BooleanField(default=True)
    is_doctor=models.BooleanField(default=False)
    line1=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=15,null=True,blank=True)
    state=models.CharField(max_length=15,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)


    # USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']
    objects=UserManager()


    def name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.username


