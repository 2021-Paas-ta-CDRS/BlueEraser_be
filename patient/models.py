from django.db import models
from user.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user', related_name='patient', primary_key=True)
    job = models.CharField(max_length=50, null=True)
