from django.db import models
from patient.models import Patient

class Question(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient', related_name='question')
    answer = models.CharField(verbose_name='답변')
    point = models.IntegerField(verbose_name='점수')
    answer_time=models.CharField(verbose_name='문답시간')
