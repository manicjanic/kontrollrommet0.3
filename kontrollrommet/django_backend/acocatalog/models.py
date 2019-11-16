from django.db import models
import uuid as uuid_field

# The Three Core Types    
ACO_TYPE = [
    ('A', 'ACTION'),
    ('C', 'CONCEPT'),
    ('O', 'OBJECT'),
]
class CoreTerm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=1, choices=ACO_TYPE, null=False) 
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Term(models.Model):
    name = models.CharField(max_length=500, unique=True, null=False) 
    core = models.ForeignKey(CoreTerm, on_delete=models.CASCADE)
    expression = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name