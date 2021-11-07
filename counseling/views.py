from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from counseling.serializers import CounselingResultSerializer, CounselingScheduleSerializer

class CounselingScheduleAPI(ModelViewSet):
    """ 상담 일정 API (의사 및 환자)
    의사 및 환자에게 호출되는 상담 일정 API
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CounselingScheduleSerializer

class CounselingResultAPI(ModelViewSet):
    """ 상담 결과 API (의사 및 환자)
    의사 및 환제에게 호출되는 상담 결과 API
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CounselingResultSerializer
