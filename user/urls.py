from django.urls import path, include
from .views import GetUserTypeAPI, LoginUserAPI

urlpatterns = [
    path('login/', LoginUserAPI.as_view()),
    path('', GetUserTypeAPI.as_view()),
]
