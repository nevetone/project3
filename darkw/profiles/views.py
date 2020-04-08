from django.shortcuts import render
from main.models import Players
from items.models import ItemsCategory, PlayerItems

# Create your views here.

def profiles(request):
    try:
        player = Players.objects.get(nickname=request.user)
    except:
        player = None
    
    items = []
    try:
        player_items = PlayerItems.objects.all()
        for players in player_items:
            if players.player == player:
                items.append(players)
    except:
        player_items = None

    
    items_category = ItemsCategory.objects.all()
    
    
    template = 'profile.html'
    context = {"player":player,'items_category':items_category,'player_items':items,}
    return render(request, template, context)