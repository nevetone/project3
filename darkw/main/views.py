from django.shortcuts import render
from .models import Players, Organizations, ChatMessages
from django.contrib.auth import get_user_model
from organization.models import OrganizationWorkers
# Create your views here.
User = get_user_model()


def index(request):
    template = 'index.html'
    context = {

    }
    return render(request, template, context)

def status(request):

    try:
        player = Players(nickname = request.user, money_bank=1, money_portfel=1, phone='22-2222')
        player.save()
    except:
        pass

    try:
        player = Players.objects.get(nickname=request.user)
    except:
        player = None


    
    template = 'status.html'
    context = {"player":player,}
    return render(request, template, context)


def SchowChatPage(request, person_name, room_name ):
    
    try:
        messages = ChatMessages.objects.filter(room_name = room_name)
    except:
        pass
    
    template = 'chat_screen.html'
    return render(request, template, {'room_name':room_name,'messages':messages, 'person_name':person_name})