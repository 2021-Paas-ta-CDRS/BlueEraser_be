from django.db import models
from django.db.models.deletion import CASCADE
from user.models import User

class Patient(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user', primary_key=True)
    job = models.CharField(max_length=50, null=True)
