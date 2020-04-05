from django.db import models
from main.models import Players, Organizations
# Create your models here.

class OrganizationWorkers(models.Model):
    organization = models.OneToOneField("main.Organizations", on_delete=models.CASCADE)
    workers = models.ManyToManyField("main.Players")
        
    def __str__(self):
        return str(self.organization)
    