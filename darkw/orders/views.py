from django.shortcuts import render
from .models import Orders, OrdersStatus, OrdersType
from main.models import Players
# Create your views here.

def orders(request):
    template = 'orders.html'
    akcept = None
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
        types = OrdersType.objects.all()
    except:
        status = None
        types = None
    try:
        akcept = request.GET.get('akcept')
    except:
        akcept = None
    
    try:
        akcept_order = Orders.objects.get(id = int(akcept))
        akcept_order.ordered_by = player
        akcept_order.status = status[1]
        akcept_order.save()
    except:
        pass
    
        

    
            
    
    context = {'status':status,'types':types,'player':player,'orders':player_orders,'all_orders':all_orders,}
    return render(request, template, context)
    