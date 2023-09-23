from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,AbstractUser
from .manager import UserManager

# Create your models here.
class Signs(AbstractUser):
    username=models.CharField(max_length=100,unique=True)
    mobile=models.CharField(max_length=10,unique=True)
    objects=UserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]
class Contacts(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    name=models.CharField(max_length=100)