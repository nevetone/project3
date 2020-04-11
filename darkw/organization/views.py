from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import Players
from django.contrib.auth import get_user_model
from items.models import ItemsCategory
from organization.models import OrganizationCars, OrganizationItems, Invites, OrganizationRanks
from .forms import InviteForm, AcceptForm, AddRank

User = get_user_model()
# Create your views here.
def organization(request):
    
    template = 'organization.html'
    player = None
    form = None
    invited_from = None
    add_form = None
    players = None
    items_category = None
    items = None
    cars = None
    
    
    # pobieranie gracza
    try:
        player = Players.objects.get(nickname=request.user)
    except:
        player = None
    # pobieranie przedmiotow organizacji
    items = []
    try:
        organization_items = OrganizationItems.objects.all()
        for item in organization_items:
            if item.organization == player.organization:
                items.append(item)
    except:
        organization_items = None
    # pobieranie samochodow organizacji
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
    # zapraszanie gracza do organzacji
    if request.method == 'POST':
        form = InviteForm(request.POST)
        if form.is_valid():
            invited = form.cleaned_data['invited']
            try:
                Users = User.objects.filter(username = invited)
                for us in Users:
                    inv = Players.objects.get(nickname = us)
                    inv.invited = True
                    send = Invites(organization = player.organization, players=inv, active = True )
                    send.save()
                    inv.save()
            except:
                pass
    else:
        form = InviteForm()
        
    # wyswietlanie zaproszen
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
    # akceptowanie zaproszen
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
    # usuwanie rang
    try:
        rank_del = request.GET.get('del')
        if player.organization_level.rank_power >= 90:
            if rank_del is not None:
                for k in player.organization.ranks.all():
                    if k.rank_name == rank_del:
                        if k.rank_power >= 100:
                            pass
                        else:
                            try:
                                player_with_ranks = Players.objects.filter(organization_level = k)
                                for i in player_with_ranks:
                                    i.organization_level = player.organization.default_rank
                                    i.save()
                            except:
                                pass
                            k.delete()
                    else:
                        pass
            else:
                pass
    except:
        pass
    # tworzenie rang
    add_form = AddRank(request.POST or None)
    if add_form.is_valid():
        rank_name = add_form.cleaned_data['rank_name']
        visible_money = add_form.cleaned_data['visible_money']
        visible_ranks = add_form.cleaned_data['visible_ranks']
        visible_chat = add_form.cleaned_data['visible_chat']
        visible_cars = add_form.cleaned_data['visible_cars']
        visible_magazine = add_form.cleaned_data['visible_magazine']
        visible_phone = add_form.cleaned_data['visible_phone']
        rank_power = add_form.cleaned_data['rank_power']
            
        if int(rank_power) >= 90:
            admin = True
        else:
            admin = False
        try:
            unique = player.organization.ranks.all()
            for u in unique:
                if u.rank_name == rank_name:
                    unique = False
                    pass
                else:
                    pass
            if unique == False:
                pass
            else:
                rank = OrganizationRanks(organization = player.organization ,rank_name = rank_name, visible_money = visible_money,\
                    visible_ranks = visible_ranks, visible_chat = visible_chat, \
                       visible_cars = visible_cars, visible_phone = visible_phone, visible_magazine = visible_magazine,\
                          rank_power = rank_power, admin = admin)
                rank.save()
                player.organization.ranks.add(rank)
                player.organization.save()
        except:
            pass
    else:
        add_form = AddRank()
    # pobeiranie kategori przedmiotow
    items_category = ItemsCategory.objects.all()

    context = {'player':player,'form':form,'add_form':add_form, 'invited_from':invited_from, 'players':players, 'items_category':items_category, 'organization_items':items,'cars':cars,}
    return render(request, template, context)



def management(request):
    template = 'management.html'
    # pobieranie gracza
    try:
        player = Players.objects.get(nickname=request.user)
    except:
        player = None
    
    
    if player.organization_level.rank_power >= 90:
        del_player = request.GET.get('del_worker')
    else:
        del_player = None
        
    try:
        if del_player is not None:
            for y in player.organization.organizationworkers.workers.all():
                if player.organization_level.rank_power > y.organization_level.rank_power:
                    if y.nickname.username == del_player:
                        y.organization = None
                        y.organization_level = None
                        y.organization_status = False
                        player.organization.organizationworkers.workers.remove(y)
                        y.save()
                        player.save()
                    else:
                        pass
    except:
        pass
    
    context ={'player':player,}
    return render(request, template, context)