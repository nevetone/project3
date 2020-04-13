from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



class Orders(models.Model):
    player = models.ForeignKey("main.Players", on_delete=models.CASCADE, blank=True, null=True)
    ordered_by = models.ForeignKey("main.Players", related_name='ordered_by', blank=True, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey("OrdersStatus", on_delete=models.CASCADE)
    order_type = models.ForeignKey("OrdersType", on_delete=models.CASCADE)
    if_kontrabanda_or_sprzedaz = models.ManyToManyField("items.PlayerItems")
    if_pranie = models.IntegerField(default=5000 , blank=True, null=True, validators=[MaxValueValidator(30000), MinValueValidator(5000)])
    if_pranie_prowizja = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(100), MinValueValidator(1)], default=10)
    received = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    class Meta:
        ordering=['-created' ,'-order_type']
    
    def __str__(self):
        return "id: " + str(self.id) + ' | ' + str(self.player) + " | " + str(self.order_type)


class OrdersStatus(models.Model):
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.status

class OrdersType(models.Model):
    order_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.order_type