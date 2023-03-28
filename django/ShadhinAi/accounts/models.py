from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
import uuid




# Create your models here.
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'profile')
    name = models.CharField(max_length= 50)
    email = models.CharField(max_length= 100)
    phone = models.IntegerField()
    image = models.ImageField(upload_to= 'user/')
    is_email_verified = models.BooleanField(default= False)
    is_phone_varified = models.BooleanField(default= False)