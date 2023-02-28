from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = email  # use email as username
        if not first_name or not last_name or not email or not password:
            return render(request, 'registration/register.html', {'error': 'All fields are required'})
        try:
            User.objects.get(email=email)
            return render(request, 'registration/register.html', {'error': 'Email already exists'})
        except ObjectDoesNotExist:
            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            print(user.get_full_name)
            # user.set_password(password)
            user.save()
            login(request, user)
            print('after login')
            return redirect('wall')
    return render(request, 'registration/register.html')


def login_view(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('wall')
    else:
        return render(request, 'registration/login.html', {'error': 'Email or password is incorrect'})
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
