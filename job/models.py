from django.db import models
from django.utils.translation import gettext_lazy as _

# in order not to duplicate the code for all models. We can create Abstract Base class
# and Inherit from the Base class

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# location is a separate model in order to add cities dynamically
class Location(TimeStampedModel):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city
    
# skill is separate model in order to add city dynamically
class Skill(TimeStampedModel):
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name

class Vacancy(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title
    
class Company(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
    

    
    

    




    
    
