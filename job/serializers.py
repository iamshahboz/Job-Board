from .models import Location, Skill, Vacancy, Company 
from rest_framework import serializers 

class LocationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Location 
        fields = ['id','city']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)
        model = Skill 
        fields = ['id','skill_name']

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)
        skills  = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(),many=True)
        model = Vacancy
        fields = ['id','title','description','salary','location','company','is_active','skills']

class CompanySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Company 
        fields = ['id','name','description','logo','verified']
        

