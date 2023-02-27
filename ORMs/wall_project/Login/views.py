from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('wall')
        else:
            user = User.objects.create_user(
                username=username, password=password)
            user.save()
            login(request, user)
            return redirect('wall')
    return render(request, 'registration/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('wall')
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
