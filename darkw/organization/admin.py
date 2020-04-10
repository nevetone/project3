from django.contrib import admin
from .models import Invites, OrganizationWorkers, OrganizationItems, OrganizationRanks, OrganizationCars

# Register your models here.

admin.site.register(OrganizationWorkers)
admin.site.register(OrganizationRanks)
admin.site.register(OrganizationCars)
admin.site.register(OrganizationItems)
admin.site.register(Invites)

