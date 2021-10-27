from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import QuestionFormSerializer
from .models import Question, QuestionForm

class QuestionFormAPI(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuestionFormSerializer
    queryset = QuestionForm.objects.all()
