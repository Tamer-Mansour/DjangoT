from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.decorators import login_required


# register method
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not (username and email and password and confirm_password):
            return render(request, 'register.html', {'error': 'All fields are required'})

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username is already taken'})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email is already taken'})

        user = User(username=username, email=email)
        user.hash_password(password)
        user.save()

        return redirect('/')

    return render(request, 'register.html')

# login method


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not (email and password):
            return render(request, 'login.html', {'error': 'Both email and password are required'})

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

        if not user.check_password(password.encode(), user.password.encode()):
            return render(request, 'login.html', {'error': 'Invalid email or password'})

        request.session['user_id'] = user.id
        return redirect('home')

    return render(request, 'login.html')

# logout method


def logout(request):
    if request.session.get('user_id'):
        del request.session['user_id']
    return redirect('/')


# edit profile method
def edit_profile(request, user_id):
    logged_in_user_id = request.session.get('user_id')
    if logged_in_user_id != user_id:
        return redirect('home')

    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        return redirect('home')

    return render(request, 'edit_profile.html', {'user': user})



# Home Page
def home(request):
    if not request.session.get('user_id'):
        return redirect('/')

    user = User.objects.get(id=request.session.get('user_id'))
    return render(request, 'home.html', {'user': user})
