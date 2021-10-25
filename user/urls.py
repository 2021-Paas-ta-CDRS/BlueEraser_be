from django.urls import path, include
from views import LoginUserAPI

urlpatterns = [
    path('login/', LoginUserAPI.as_view()),
]
