from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Players(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE)
    money_bank = models.IntegerField(default=0)
    money_portfel = models.IntegerField(default=0)
    phone = models.CharField(max_length=7, default=00-0000)
    organization_status = models.BooleanField(default=False)  
    organization = models.ForeignKey('Organizations', on_delete=models.CASCADE, blank=True, null=True)
    organization_level = models.ForeignKey("organization.OrganizationRanks", on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateField(auto_now=False, auto_now_add=True)
    invited = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-organization_level']
    
    
    def __str__(self):
        return str(self.nickname)
    

class Organizations(models.Model):
    boss = models.OneToOneField(Players, on_delete=models.CASCADE, blank=True, null=True)
    organization_name = models.CharField(max_length=50, unique=True)
    money = models.IntegerField()
    ranks = models.ManyToManyField("organization.OrganizationRanks", related_name="Rangi", blank=True, null=True )
    activated = models.BooleanField(default=False)
    created = models.DateField(auto_now=False, auto_now_add=True)
    default_rank = models.ForeignKey("organization.OrganizationRanks", related_name="default_rank", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.organization_name)

