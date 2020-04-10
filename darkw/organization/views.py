from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import Players
from items.models import ItemsCategory
from organization.models import OrganizationCars, OrganizationItems, Invites, Organization
from .forms import InviteForm, AcceptForm


# Create your views here.
def organization(request):
    
    template = 'organization.html'
    player = None
    form = None
    invited_from = None
    players = None
    items_category = None
    items = None
    cars = None
    
    

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
        
    try:
        players = Players.objects.all()
    except:
        players = None
    
    

    if request.method == 'POST':
        form = InviteForm(request.POST)
        if form.is_valid():
            invited = form.cleaned_data['invited']
            
    else:
        form = InviteForm()
        
    
    try:
        players_invites = Invites.objects.all()
        for x in players_invites:
            to = x.organization
            who = x.players
            if who == player:
                invited_from = to
            else:
                invited_from = None
    except:
        players_invites = None
        invited_from = None
        
        
    try:
        accept = request.GET.get('accept')
    except:
        accept = None
    
    
    try:
        if invited_from is not None:
            if accept == "False":
                invite = Invites.objects.get(players = player)
                player.invited = False
                player.save()
                invite.delete()
            elif accept == "True":
                invite = Invites.objects.get(players = player)
                player.organization = invited_from
                player.organization_status = True
                player.organization.organizationworkers.workers.add(player)
                player.organization_level = player.organization.default_rank
                player.invited = False
                player.save()
                invite.delete()
    except:
        invite = None
    
    
    items_category = ItemsCategory.objects.all()

    context = {'player':player,'form':form, 'invited_from':invited_from, 'players':players, 'items_category':items_category, 'organization_items':items,'cars':cars,}
    return render(request, template, context)


    
