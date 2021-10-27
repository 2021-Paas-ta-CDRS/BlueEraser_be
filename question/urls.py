from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionFormAPI, QuestionAPI

router = DefaultRouter()
router.register(r'question_form', QuestionFormAPI)
router.register(r'', QuestionAPI, basename='question')
urlpatterns = [
    path('', include(router.urls)),
]
