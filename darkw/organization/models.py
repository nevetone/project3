from django.db import models
from main.models import Players, Organizations
# Create your models here.

class OrganizationWorkers(models.Model):
    organization = models.OneToOneField("main.Organizations", on_delete=models.CASCADE)
    workers = models.ManyToManyField("main.Players")
        
    def __str__(self):
        return str(self.organization)
    
    
    
class OrganizationRanks(models.Model):
    organization = models.ForeignKey("main.Organizations", on_delete=models.CASCADE)
    rank_name = models.CharField(max_length=20, default="Rekrut")
    visible_money = models.BooleanField(default=False)
    visible_ranks = models.BooleanField(default=False)
    visible_chat = models.BooleanField(default=False)
    visible_cars = models.BooleanField(default=False)
    visible_magazine =models.BooleanField(default=False)
    visible_phone = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    rank_power = models.IntegerField(default=0)
    
    class Meta:
        ordering=['-rank_power']
    
    def __str__(self):
        return str(self.organization) + " | " + str(self.rank_name)
    
    
    

class OrganizationCars(models.Model):
    organization = models.ForeignKey("main.Organizations", on_delete=models.CASCADE, blank=True, null=True)
    car = models.ForeignKey("items.Cars", on_delete=models.CASCADE, blank=True, null=True)
    cars_count = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.organization) + " " + str(self.car)
    
class OrganizationItems(models.Model):
    organization = models.ForeignKey("main.Organizations", on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey("items.Items", on_delete=models.CASCADE, blank=True, null=True)
    item_count = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.organization) + " " + str(self.item)
    
class Invites(models.Model):
    organization = models.ForeignKey("main.Organizations", on_delete=models.CASCADE)
    players = models.OneToOneField("main.Players", on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.players) + " invited by: " + str(self.organization)
    