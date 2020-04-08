from django.shortcuts import render
from main.models import Players
from items.models import ItemsCategory
from organization.models import OrganizationCars, OrganizationItems

# Create your views here.
def organization(request):
    template = 'organization.html'
    try:
        player = Players.objects.get(nickname=request.user)
    except:
        player = None

        
    items = []
    try:
        organization_items = OrganizationItems.objects.all()
        for item in organization_items:
            if item.organization == player.organization:
                items.append(item)
    except:
        organization_items = None
    
    cars = []
    try:
        organization_cars = OrganizationCars.objects.all()
        for car in organization_cars:
            if car.organization == player.organization:
                cars.append(car)
    except:
        cars = None
        

    items_category = ItemsCategory.objects.all()

    context = {'player':player,'items_category':items_category, 'organization_items':items,'cars':cars,}
    return render(request, template, context)