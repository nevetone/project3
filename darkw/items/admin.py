from django.contrib import admin
from .models import ItemsCategory, Items, PlayerItems, Cars, CarsCategory
# Register your models here.

admin.site.register(ItemsCategory)
admin.site.register(Items)
admin.site.register(PlayerItems)
admin.site.register(Cars)
admin.site.register(CarsCategory)
