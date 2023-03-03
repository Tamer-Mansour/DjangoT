from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import hashlib
import random
import string
from django.core.mail import send_mail
from .models import *


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Generate verification code
        verification_code = ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(32))
        verification_code = hashlib.sha256(
            verification_code.encode()).hexdigest()

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.email_verification_code = verification_code
        user.save()

        # Send verification email
        subject = 'Verify your email address'
        message = 'Please click the link below to verify your email address:\n'
        message += request.build_absolute_uri(
            f'/verify_email/{verification_code}/')
        from_email = 'tmansour720@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        return redirect('login')
    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('user_list')
            else:
                return redirect('profile')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'login.html')


def verify_email(request, verification_code):
    user = User.objects.filter(
        email_verification_code=verification_code).first()
    if user:
        user.is_email_verified = True
        user.email_verification_code = None
        user.save()
        return render(request, 'email_verified.html')
    else:
        return render(request, 'verification_failed.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def user_list(request):
    if request.user.is_superuser:
        users = User.objects.all()
        return render(request, 'user_list.html', {'users': users})
    else:
        return redirect('profile')


@login_required
def user_edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('user_list')
    return render(request, 'user_edit.html', {'user': user})


@login_required
def user_delete(request, pk):
    User.objects.get(pk=pk).delete()
    return redirect('user_list')
