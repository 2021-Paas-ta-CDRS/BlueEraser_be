from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from .serializers import QuestionFormSerializer
from .models import Question, QuestionForm

class CreateQuestionFormAPI(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuestionFormSerializer
    queryset = QuestionForm
