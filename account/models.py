from django.db import models
from job.models import Skill

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

class Candidate(TimeStampedModel):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    photo = models.ImageField()
    education = models.ManyToManyField(University, related_name='candidates_attended')
    class DegreeChoices(models.TextChoices):
        BACHELORS = "B.S.", ('Bachelors')
        MASTERS = "M.S.", ('Masters')
        DOCTOR = "Ph.D.", ('Ph.D.')
    degree = models.CharField(max_length=20, choices=DegreeChoices.choices)
    skill = models.ManyToManyField(Skill, related_name='candidates_with_skill')

    def __str__(self):
        return self.name 
    

