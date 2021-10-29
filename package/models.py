from django.db import models
from doctor.models import Doctor

class Package(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column='doctor', related_name='package')
    package_name = models.CharField(max_length=100, verbose_name='상품명')
    price = models.IntegerField(verbose_name='가격')
    count = models.IntegerField(verbose_name='횟수')
    description = models.TextField(verbose_name='상품 설명')
    counseling_time = models.IntegerField(verbose_name='상담 시간')
    is_active = models.BooleanField(verbose_name='활성')
