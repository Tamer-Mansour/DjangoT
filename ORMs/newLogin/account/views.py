from django.shortcuts import render, redirect
from .models import User


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        user = User(username=username, email=email)
        user.hash_password(password)
        user.save()

        return redirect('login')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

        if user.check_password(request.POST['password'].encode(), user.password.encode() ):
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')


def home(request):
    if not request.session.get('user_id'):
        return redirect('login')

    user = User.objects.get(id=request.session.get('user_id'))
    return render(request, 'home.html', {'user': user})


def logout(request):
    if request.session.get('user_id'):
        del request.session['user_id']

    return redirect('login')
