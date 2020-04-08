from django.db import models

# Create your models here.



class ItemsCategory(models.Model):
    item_category = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return str(self.item_category)
    
class Items(models.Model):
    item_category = models.ForeignKey(ItemsCategory, on_delete=models.CASCADE, blank=True, null=True)
    item_name = models.CharField(max_length=50, default='item')
    
    def __str__(self):
        return str(self.item_name)
    
class PlayerItems(models.Model):
    player = models.ForeignKey("main.Players", on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey("Items", on_delete=models.CASCADE, blank=True, null=True)
    item_count = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.player) + " " + str(self.item)
    
class OrganizationItems(models.Model):
    organization = models.ForeignKey("main.Organizations", on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey("Items", on_delete=models.CASCADE, blank=True, null=True)
    item_count = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.organization) + " " + str(self.item)