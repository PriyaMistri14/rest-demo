from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    username = models.CharField(blank=True, null=True)
    email = models.EmailField(_(), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
