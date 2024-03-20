from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf.urls import static 
from django.conf import settings



urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('location/', views.LocationListCreate.as_view()),
    path('location/<int:pk>/', views.LocationEdit.as_view()),
    path('skill/',views.SkillListCreate.as_view()),
    path('skill/<int:pk>/',views.SkillEdit.as_view()),
    path('vacancy/',views.VacancyListCreate.as_view()),
    path('vacancy/<int:pk>/',views.VacancyEdit.as_view()),
    path('company/',views.CompanyListCreate.as_view()),
    path('company/<int:pk>/',views.CompanyEdit.as_view()),
    path('candidate/',views.CandidateListCreate.as_view()),
    path('candidate/<int:pk>',views.CandidateEdit.as_view()),
    
] 
