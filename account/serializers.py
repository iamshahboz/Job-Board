from rest_framework import serializers 
from .models import User, University, Skill
from job.serializers import SkillSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# since skill has ManyToManyField in the database level
# we have defined it with PrimaryKeyRelatedField and set many to True

class UniversitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = University
        fields = ['id','name']

        

class CandidateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    

    class Meta:
        model = User
        fields = ['id', 'surname', 'name', 'email', 'password', 'password2']


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            surname = validated_data['surname'],  
            name = validated_data['name'],   
            email=validated_data['email'],
            role = User.RoleChoices.CANDIDATE
        )
        user.set_password(validated_data['password'])
        user.save()
        return user 
    

class CandidateEdit(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User 
        fields = ['id','surname','name','date_of_birth','photo','education','degree','skill','phone']
        
    
        

    







