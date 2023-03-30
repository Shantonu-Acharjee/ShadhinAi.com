from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.


# create model for user
class User(AbstractUser):
    email = models.EmailField(max_length= 150, unique= True, error_messages= {'unique' : 'Email must be unique'})
    profile_image = models.ImageField(upload_to= 'profile_images', null= True, blank= True)


    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
