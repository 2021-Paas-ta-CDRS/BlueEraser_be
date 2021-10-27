from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import QuestionFormSerializer, QuestionSerializer
from .models import Question, QuestionForm

class QuestionFormAPI(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = QuestionFormSerializer
    queryset = QuestionForm.objects.all()

class QuestionAPI(ListModelMixin, CreateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        # 점수 계산 로직 구현 필요함
        serializer = self.get_serializer(data={'patient': request.user.patient, 'point': 100, **request.data.dict()})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return Question.objects.filter(patient=self.request.user.patient)
