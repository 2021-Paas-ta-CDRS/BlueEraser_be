from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionFormAPI

router = DefaultRouter()
router.register(r'question_form', QuestionFormAPI)
urlpatterns = [
    path('', include(router.urls)),
]
