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
            user_type = kwargs.get('user_type'),
            email=self.normalize_email(kwargs.get('email'))
        )
        user.set_password(self.normalize_email(kwargs.get('password')))
        user.save(using=self._db)
        return user
    
    def create_superuser(self, **kwargs):
        new_superuser = self.create_user(**kwargs)
        new_superuser.is_admin = True
        new_superuser.save(using=self._db)
        return new_superuser
        
class User(AbstractBaseUser):

    class USER_CHOICE(models.TextChoices):
        PATIENT = ('P', 'Patient')
        DOCTOR = ('D', 'Doctor')

    class SEX_CHOICE(models.TextChoices):
        MALE = ('M', 'Male')
        FEMALE = ('F', 'Female')

    email = models.EmailField(verbose_name='이메일', max_length=255, unique=True)
    name = models.CharField(max_length=30, verbose_name='이름', null=True)
    age = models.IntegerField(verbose_name='나이', null=True)
    phone_number = models.CharField(max_length=20, verbose_name='전화번호', null=True)
    sex = models.CharField(max_length=2, choices=SEX_CHOICE.choices, verbose_name='성별', null=True)
    address = models.CharField(max_length=200, verbose_name='주소', null=True)
    joined_date = models.DateTimeField(auto_now_add=True, verbose_name='가입년월일')
    
    user_type = models.CharField(max_length=2, choices=USER_CHOICE.choices, verbose_name="유저타입")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
