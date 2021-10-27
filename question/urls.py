from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionFormAPI

urlpatterns = [
    path('question_form/', QuestionFormAPI.as_view()),
]
