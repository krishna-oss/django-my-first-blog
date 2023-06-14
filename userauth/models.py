from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12,unique=True)
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username','phone_number']

    def __str__(self):
        return self.username