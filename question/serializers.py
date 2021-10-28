from rest_framework import serializers
from .models import Question, QuestionForm

class QuestionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionForm
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
