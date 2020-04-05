from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Players(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE)
    money_bank = models.IntegerField(default=0)
    money_portfel = models.IntegerField(default=0)
    organization_status = models.BooleanField(default=False)  
    organization = models.ForeignKey('Organizations', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return str(self.nickname)
    

class Organizations(models.Model):
    boss = models.OneToOneField(Players, on_delete=models.CASCADE, blank=True, null=True)
    organization_name = models.CharField(max_length=50, unique=True)
    money = models.IntegerField()
    activated = models.BooleanField(default=False)
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.organization_name)

