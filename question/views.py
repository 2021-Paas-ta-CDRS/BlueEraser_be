from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import QuestionFormSerializer
from .models import Question, QuestionForm

class QuestionFormAPI(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = QuestionFormSerializer
    queryset = QuestionForm.objects.all()
