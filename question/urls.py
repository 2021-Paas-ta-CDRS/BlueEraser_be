from django.urls import path, include
from .views import CreateQuestionFormAPI

urlpatterns = [
    path('', CreateQuestionFormAPI.as_view()),
]
