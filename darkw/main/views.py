from django.shortcuts import render

# Create your views here.

def index(request):
    template = 'index.html'
    context = {

    }
    return render(request, template, context)

def status(request):
    template = 'status.html'
    context = {

    }
    return render(request, template, context)