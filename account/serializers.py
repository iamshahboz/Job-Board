from rest_framework import serializers 
from .models import Candidate, University, Skill

# since skill has ManyToManyField in the database level
# we have defined it with PrimaryKeyRelatedField and set many to True

class CandidateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    education = serializers.PrimaryKeyRelatedField(queryset=University.objects.all(),many=True)
    skill = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(),many=True)
    class Meta:
        model = Candidate 
        fields = ['id','surname','name','date_of_birth','photo','education','degree','skill']

class UniversitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = University
        fields = ['id','name']