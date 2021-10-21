from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.LoginUserAPI.as_view()),
    path('test/', views.TestTokenAPI.as_view()),
    path('update/<int:pk>', views.UpdateUserAPI.as_view()),
]
