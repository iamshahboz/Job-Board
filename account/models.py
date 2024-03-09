from django.db import models
from job.models import Skill

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
    education = models.ForeignKey(University, on_delete=models.CASCADE, blank=True, null=True)
    class DegreeChoices(models.TextChoices):
        BACHELORS = "B.S.", ('Bachelors')
        MASTERS = "M.S.", ('Masters')
        DOCTOR = "Ph.D.", ('Ph.D.')
    degree = models.CharField(max_length=20, choices=DegreeChoices.choices)
    skill = models.ManyToManyField(Skill, related_name='candidates')

    def __str__(self):
        return self.name 
    

