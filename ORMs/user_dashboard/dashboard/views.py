from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import *

def index(request):
    return render(request, 'user_app/index.html')


def login_page(request):
    return render(request, 'user_app/login.html')


def register_page(request):
    return render(request, 'user_app/register.html')


def dashboard(request):
    return render(request, 'user_app/dashboard.html', {'user_data': User.objects.all()})


def users_new(request):
    return render(request, 'user_app/users_new.html')


def users_homepage(request, id):
    user = User.objects.filter(id=id)
    for user in user:
        context = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'id': user.id,
            'email': user.email,
            'description': user.description,
            'user_level': user.user_level,
            'created_at': user.created_at,
        }

    return render(request, 'user_app/users_homepage.html', context)


import bcrypt

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)
            request.session['user_id'] = user.id
            request.session['user_name'] = user.first_name
            return redirect('/dashboard')

    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
        except:
            messages.error(request, "Invalid email or password")
            return redirect('/login')
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            request.session['user_name'] = user.first_name
            return redirect('/dashboard')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('/login')
    
    return render(request, 'login.html')


def logout(request):
    request.session['login_status'] = 0
    del request.session['id']
    del request.session['user_level']
    return redirect('/login')


def edit(request, id):  
    context = {
        'user_data': User.objects.filter(id=id)
    }
    return render(request, 'user_app/edit.html', context)


def edit_users(request):
    user = User.objects.get(id=request.POST['id'])
    if request.POST['submit'] == 'Save':
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.user_level = request.POST['user_level']
        user.save()
        return redirect('/dashboard')

    if request.POST['submit'] == 'Update Password':
        errors = User.objects.password_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/edit/'+str(user.id))

        password = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt())
        user.password = password
        user.save()
        return redirect('/dashboard')

    if request.POST['submit'] == 'Edit Description':
        user.description = request.POST['description']
        user.save()
        return redirect('/dashboard')


def delete(request, id):
    User.objects.get(id=id).delete()

    return redirect('/dashboard')
