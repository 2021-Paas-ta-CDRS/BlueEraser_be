from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        if not "email" in kwargs:
            raise ValueError("Users must have an email")
        if not "password" in kwargs:
            raise ValueError("Users must have a password")
        user = self.model(
            email=self.normalize_email(kwargs.get("email")),
            name=kwargs.get("name"),
        )
        
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=30)
    