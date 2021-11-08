from rest_framework import serializers
from .models import CounselingResult, CounselingSchedule

class CounselingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounselingSchedule
        fields = '__all__'

class CounselingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounselingResult
        fields = '__all__'
