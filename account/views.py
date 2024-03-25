
from .serializers import CandidateSerializer, UniversitySerializer,CandidateEdit
from .models import User, University
from rest_framework import generics
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status



# views for each model created
# order is -id and it means that the last created item comes first

class CandidateListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = CandidateSerializer




class CandidateEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = CandidateEdit

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response

class UniversityListCreate(generics.ListCreateAPIView):
    queryset = University.objects.all().order_by('-id')
    serializer_class = UniversitySerializer

class UniversityEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all().order_by('-id')
    serializer_class = UniversitySerializer




    
