from account.models import User
from django.http import HttpResponse
from rest_framework import generics
from account.serializers import CandidateSerializer
from .models import Location, Skill, Vacancy, Company
from .serializers import (
    LocationSerializer, SkillSerializer, VacancySerializer, CompanySerializer
                        )


def homepage(request):
    return HttpResponse("<center>Hello, world. You're at the jobs homepage.</center>")



class LocationListCreate(generics.ListCreateAPIView):
    queryset = Location.objects.all().order_by('-id')
    serializer_class = LocationSerializer

class LocationEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all().order_by('-id')
    serializer_class = LocationSerializer

class SkillListCreate(generics.ListCreateAPIView):
    queryset = Skill.objects.all().order_by('-id')
    serializer_class = SkillSerializer

class SkillEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all().order_by('-id')
    serializer_class = SkillSerializer 

class VacancyListCreate(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all().order_by('-id')
    serializer_class = VacancySerializer

class VacancyEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all().order_by('-id')
    serializer_class = VacancySerializer

class CompanyListCreate(generics.ListCreateAPIView):
    queryset = Company.objects.all().order_by('-id')
    serializer_class = CompanySerializer

class CompanyEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all().order_by('-id')
    serializer_class = CompanySerializer

class CandidateListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = CandidateSerializer

    def perform_create(self, serializer):
        serializer.save(role=User.RoleChoices.CANDIDATE)

class CandidateEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = CandidateSerializer
    




    



