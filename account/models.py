from django.db import models
from job.models import Skill
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user 
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **extra_fields)
        
    


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
    

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class User(AbstractBaseUser, PermissionsMixin):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to ='candidates/')
    education = models.ManyToManyField(University, related_name='candidates_attended')
    class DegreeChoices(models.TextChoices):
        BACHELORS = "B.S.", ('Bachelors')
        MASTERS = "M.S.", ('Masters')
        DOCTOR = "Ph.D.", ('Ph.D.')
    degree = models.CharField(max_length=20, choices=DegreeChoices.choices)
    skill = models.ManyToManyField(Skill, related_name='candidates_with_skill')
    phone = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)   
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True) # a admin user; non super-user
    is_superuser = models.BooleanField(default=True) # a superuser
    class Status(models.IntegerChoices):
        ACTIVE = 1
        NOT_ACTIVE = 0
    status = models.IntegerField(choices=Status.choices,default=1)
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
     
    

