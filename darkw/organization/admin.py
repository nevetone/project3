from django.contrib import admin
from .models import OrganizationWorkers, OrganizationRanks, Organization, OrganizationCars

# Register your models here.

admin.site.register(OrganizationWorkers)
admin.site.register(OrganizationRanks)
admin.site.register(Organization)
admin.site.register(OrganizationCars)

