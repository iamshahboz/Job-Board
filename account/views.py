from django.shortcuts import render
from .serializers import CandidateSerializer, UniversitySerializer
from .models import User, University
from rest_framework import generics

# views for each model created
# order is -id and it means that the last created item comes first

class CandidateListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = CandidateSerializer

class CandidateEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = CandidateSerializer

class UniversityListCreate(generics.ListCreateAPIView):
    queryset = University.objects.all().order_by('-id')
    serializer_class = UniversitySerializer

class UniversityEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all().order_by('-id')
    serializer_class = UniversitySerializer

    
