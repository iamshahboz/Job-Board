from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings


from . import views 

urlpatterns = [
    #path('', views.homepage, name='homepage'),

    path('candidate/', views.CandidateListCreate.as_view()),
    path('candidate/<int:pk>/',views.CandidateEdit.as_view()),
    path('university/',views.UniversityListCreate.as_view()),
    path('university/<int:pk>/',views.UniversityEdit.as_view()),

] 
