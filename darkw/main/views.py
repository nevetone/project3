from django.shortcuts import render
from .models import Players, Organizations
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
        player = Players(nickname = request.user , money = 0)
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