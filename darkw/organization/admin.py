from django.contrib import admin
from .models import OrganizationWorkers, OrganizationItems, OrganizationRanks, Organization, OrganizationCars

# Register your models here.

admin.site.register(OrganizationWorkers)
admin.site.register(OrganizationRanks)
admin.site.register(Organization)
admin.site.register(OrganizationCars)
admin.site.register(OrganizationItems)

