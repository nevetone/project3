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
        
    # akceptowanie zlecenia
    try:
        akcept = request.GET.get('akcept')
    except:
        akcept = None
    
    try:
        akcept_order = Orders.objects.get(id = int(akcept))
        if akcept_order.player == player:
            pass
        else:
            akcept_order.ordered_by = player
            akcept_order.status = status[1]
            akcept_order.save()
    except:
        pass
    
    
    # usuwanie zlecenia
    try:
        del_order = request.GET.get('del_order')
    except:
        del_order = None
    
    try:
        del_order = Orders.objects.get(id = int(del_order))
        if del_order.player == player:
            del_order.delete()
            pass
        else:
            pass
    except:
        pass
        
    try:
        get_order = request.GET.get('get_order')
    except:
        get_order = None
    
    # odbieranie zlecenia
    try:
        get_order = Orders.objects.get(id = int(get_order))
        if get_order.status == status[3]:
            if get_order.player == player:
                get_order.received = True
                get_order.status = status[2]
                get_order.save()
                pass
            else:
                pass
        else:
            pass
    except:
        pass
    
    context = {'status':status,'types':types,'player':player,'orders':player_orders,'all_orders':all_orders,}
    return render(request, template, context)
    