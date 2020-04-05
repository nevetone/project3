from django.shortcuts import render
from main.models import Players

# Create your views here.
def organization(request):
    template = 'organization.html'
    try:
        player = Players.objects.get(nickname=request.user)
    except:
        player = None

    context = {'player':player,}
    return render(request, template, context)