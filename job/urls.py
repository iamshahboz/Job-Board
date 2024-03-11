from django.urls import path, include
from rest_framework import routers
from . import views



urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('location/', views.LocationListCreate.as_view()),
    path('location/<int:pk>/', views.LocationEdit.as_view()),
]
