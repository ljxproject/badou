from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.
class User(AbstractBaseUser):
    mobile = models.CharField(max_length=11, verbose_name='手机号码', unique=True)
    objects = UserManager()
    USERNAME_FIELD = 'mobile'
