from django.db import models
from django.db.models.fields import BooleanField, CharField, TextField
from user.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user', related_name='doctor', primary_key=True)
    hospital_address = CharField(max_length=200, verbose_name='병원주소', null=True)
    is_verified = BooleanField(verbose_name='인가여부', null=True)
    self_pr = TextField(verbose_name='자기소개', null=True)