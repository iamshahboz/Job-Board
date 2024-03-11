from .models import Location, Skill, Vacancy, Company 
from rest_framework import serializers 

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location 
        fields = ['city']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill 
        fields = ['skill_name']

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['title','description','salary','location','company','is_active','skills']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company 
        fields = ['name','description','logo','verified']
        

