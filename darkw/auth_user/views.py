from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import LoginForm, RegistrationForm
# Create your views here.


def logout_view(request):
    logout(request)
    messages.success(request, "Wylogowano, Zapraszamy ponownie.")
    return HttpResponseRedirect('%s' % reverse('index'))

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect('/status/')
    else:
        messages.error(request, "Nie udało się zalogować")
        is_error = True
    context={"form":form, "is_error":is_error,}
    return render(request, "index.html", context)

def registration_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()
        messages.success(request, "Rejestracja pomyślna")
        is_error = False
    else:
        messages.error(request, "Nie udało się Zarejestrować - Spróbuj ponownie")
        is_error = True
    context={"form":form, "is_error":is_error,}
    return render(request, "index.html", context)