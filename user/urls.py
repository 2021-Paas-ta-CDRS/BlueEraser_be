from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('signup/', views.CreateUserAPI.as_view()),
]
