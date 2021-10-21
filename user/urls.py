from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.LoginUserAPI.as_view()),
    path('update/', views.UpdateUserAPI.as_view()),
]
