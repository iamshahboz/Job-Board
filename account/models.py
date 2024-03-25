from django.db import models
from job.models import Skill
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    def create_superuser(self,email,role,password,**other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('surname', 'Admin')
        other_fields.setdefault('name', 'Admin')
        other_fields.setdefault('date_of_birth', '2000-01-01')
        other_fields.setdefault('phone', 900000100)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email,role,password, **other_fields)

    def create_user(self,email,role,password,**other_fields):
        user = self.model(email=email, role=role,
                            password=password,**other_fields)
        user.set_password(password)
        user.save()
        return user

        

# in order to add created_at, updated_at fields to all models this model created
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class University(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.now)
    photo = models.ImageField(upload_to ='candidates/')
    education = models.ManyToManyField(University, related_name='candidates_attended')
    class DegreeChoices(models.TextChoices):
        BACHELORS = "B.S.", ('Bachelors')
        MASTERS = "M.S.", ('Masters')
        DOCTOR = "Ph.D.", ('Ph.D.')
    degree = models.CharField(max_length=20, choices=DegreeChoices.choices)
    skill = models.ManyToManyField(Skill, related_name='candidates_with_skill')
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    class RoleChoices(models.IntegerChoices):
        ADMIN = 1, "Admin"
        CANDIDATE = 2, "Candidate"
        EMPLOYEE = 3, "Employee"
        MODERATOR = 4, "Moderator"
    role = models.IntegerField(choices=RoleChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    # this method allows you to delete the file from media root, while delete method called
    def delete(self):
        self.photo.delete()
        super().delete()

    def __str__(self):
        return self.email
     
    

