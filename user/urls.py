from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('login/', views.LoginUserAPI.as_view()),
    path('test/', views.TestTokenAPI.as_view()),
]
