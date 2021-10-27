from django.db import models
from patient.models import Patient

class QuestionForm(models.Model):
    question_form_name = models.CharField(max_length=50, verbose_name='문답지이름', default='')
    form = models.JSONField()

class Question(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient', related_name='question')
    question_form = models.ForeignKey(QuestionForm, on_delete=models.CASCADE, db_column='question_form', related_name='question_form')
    answer = models.JSONField(verbose_name='답변')
    point = models.IntegerField(verbose_name='점수')
    answer_time=models.DateTimeField(auto_now_add=True, verbose_name='문답일자')
