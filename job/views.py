from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Location, Skill, Vacancy, Company
from .serializers import (
    LocationSerializer, SkillSerializer, VacancySerializer, CompanySerializer
                        )


def homepage(request):
    return HttpResponse("<center>Hello, world. You're at the jobs homepage.</center>")

# LC means ListCreate
# RUD

class LocationListCreate(generics.ListCreateAPIView):
    queryset = Location.objects.all().order_by('-id')
    serializer_class = LocationSerializer

class LocationEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all().order_by('-id')
    serializer_class = LocationSerializer
    



