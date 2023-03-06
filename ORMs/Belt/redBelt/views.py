from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib import messages


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
    quotes = Quote.objects.all()
    if not request.session.get('user_id'):
        return redirect('/')

    user = User.objects.get(id=request.session.get('user_id'))
    context = {
        'user': user,
        'quotes': quotes,
    }
    return render(request, 'home.html', context)

# add quote method


def quotes(request):
    quotes = Quote.objects.all()
    user = User.objects.get(id=request.session.get('user_id'))
    context = {
        'quotes': quotes,
        'user': user
    }
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        user_id = request.session.get('user_id')

        if user_id:
            user = User.objects.get(id=user_id)
            quote = Quote(author=author, text=text, addby=user)
            quote.save()

        # Redirect to the same page after adding a new quote
        return redirect('quotes')

    return render(request, 'quotes.html', context)


def view_quotes(request):
    quotes = Quote.objects.all()
    user_id = request.session.get('user_id')

    return render(request, 'quotes.html', {'quotes': quotes, 'user_id': user_id})


def user_quotes(request, user_id):
    user = User.objects.get(id=user_id)
    quotes = Quote.objects.filter(addby=user)
    return render(request, 'user_quotes.html', {'user': user, 'quotes': quotes})


# delete quote method
def delete_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    user_id = request.session.get('user_id')
    if not user_id or quote.addby_id != user_id:
        messages.error(request, 'User not authenticated or not authorized')
    else:
        quote.delete()
        messages.success(request, 'Quote deleted')

    return redirect('quotes')


def like_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'User not authenticated')
        return redirect('quotes')

    if LikedQuote.objects.filter(quote=quote, user_id=user_id).exists():
        messages.error(request, 'Quote already liked')
        return redirect('quotes')

    like = LikedQuote(quote=quote, user_id=user_id)
    like.save()

    messages.success(request, 'Quote liked')
    return redirect('quotes')


def unlike_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    like = LikedQuote.objects.filter(quote=quote, user_id=user_id)
    if not like.exists():
        message = 'Quote not liked'
    else:
        like.delete()
        message = 'Quote unliked'

    # Redirect to the previous page
    return redirect(request.META.get('HTTP_REFERER'), message=message)
