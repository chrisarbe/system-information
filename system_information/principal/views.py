from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'mesage':'Bienvenido',
            'code':'1'
            })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'mesage':'Usuario o Clave no válidos',
                'code':'2'
                })
        else:
            login(request, user)
            return redirect('dashboard')


def signout(request):
    logout(request)
    return redirect('login')

