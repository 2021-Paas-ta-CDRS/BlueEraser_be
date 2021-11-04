from django.db import models
from doctor.models import Doctor
from patient.models import Patient

class Package(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, db_column='doctor', related_name='package')
    package_name = models.CharField(max_length=100, verbose_name='상품명')
    price = models.PositiveIntegerField(verbose_name='가격')
    count = models.PositiveSmallIntegerField(verbose_name='횟수')
    description = models.TextField(verbose_name='상품 설명')
    counseling_time = models.IntegerField(verbose_name='상담 시간')
    is_active = models.BooleanField(verbose_name='활성', default=True)

class Matching(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient', related_name='matching')
    package = models.ForeignKey(Package, on_delete=models.PROTECT, db_column='package', related_name='matching')
    state = models.BooleanField(default=True, verbose_name='매칭상태')

class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, db_column='doctor', related_name='review')
    matching = models.ForeignKey(Matching, on_delete=models.PROTECT, db_column='matching', related_name='review')
    star_rating = models.PositiveSmallIntegerField(verbose_name='별점')
    comment = models.TextField(verbose_name='설명')
