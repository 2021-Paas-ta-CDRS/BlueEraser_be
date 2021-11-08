from django import db
from django.db import models
from django.db.models.deletion import PROTECT

from package.models import Matching

class CounselingSchedule(models.Model):
    matching = models.ForeignKey(Matching, on_delete=models.PROTECT, related_name='counseling_schedule', db_column='matching')
    start_datetime = models.DateField(verbose_name='상담일자및시간')
    is_valid = models.BooleanField(verbose_name='승인여부')
    end_datetime = models.DateField(verbose_name='상담종료및시간')
    state = models.BooleanField(default=False, verbose_name='상담상태')

class CounselingResult(models.Model):
    counseling_schedule = models.OneToOneField(CounselingSchedule, on_delete=PROTECT, related_name='counseling_result', db_column='counseling_result')
    prescription = models.TextField(verbose_name='처방')
    doctor_memo = models.TextField(verbose_name='의사 메모')
    content = models.TextField(verbose_name='상담내용')
