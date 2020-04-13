from django.shortcuts import render
from .models import Orders, OrdersStatus, OrdersType
from main.models import Players
# Create your views here.

def orders(request):
    template = 'orders.html'
    
    player = None
    # pobieranie gracza
    try:
        player = Players.objects.get(nickname=request.user)
    except:
        player = None
    try:
        all_orders = Orders.objects.all()
    except:
        all_orders = None
    try:
        player_orders = Orders.objects.filter(player = player)
    except:
        player_orders = None
    try:
        status = OrdersStatus.objects.all()
        print(status)
    except:
        status = None
    


    
    
    context = {'status':status,'player':player,'orders':player_orders,'all_orders':all_orders,}
    return render(request, template, context)
    