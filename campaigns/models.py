from django.db import models

# Create your models here.
class Campaign(models.Model):
    name=models.CharField(max_length=33)
    home=models.CharField(max_length=33)
    
    def __str__(self):
        return f"{self.name} ({self.home})"
    

class Vacancy(models.Model):
    employer=models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="company")
    requirements=models.CharField(max_length=500)
    role=models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.id}: {self.employer} offers role {self.role} requirements:{self.requirements}"
    
    
class Employee(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    registered=models.ManyToManyField(Vacancy, blank=True, related_name="employees")
    
    def __str__(self):
        return f"{self.first} {self.last}"     