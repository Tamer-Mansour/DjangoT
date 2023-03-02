from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    return render(request, 'wall_app/index.html')


def register(request):
    errors = User.objects.reg_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(
            request.POST['pword'].encode(), salt)
        user = User.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email_address=request.POST['email'],
            password=password,
            # salt=salt
        )
        request.session['user'] = user.id
        request.session['fname'] = user.first_name
    return redirect('/wall')


# def login(request):
#     errors = User.objects.log_validation(request.POST)
#     if len(errors) > 0:
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect('/')
#     else:
#         user = User.objects.get(email_address=request.POST['email'])
#         if bcrypt.checkpw(request.POST['pword'].encode(), user.password.encode()):
#             request.session['user'] = user.id
#             request.session['fname'] = user.first_name
#             return redirect('/wall')
#         else:
#             messages.error(request, 'Invalid email or password')
#             return redirect('/')

def login(request):
    if request.method == 'POST':
        email_address = request.POST.get('email')
        # password = request.POST['pword']
        try:
            user = User.objects.get(email_address=email_address)
        except User.DoesNotExist:
            return render(request, 'wall_app/index.html', {'error': 'Invalid email or password'})

        if user.check_password(request.POST['pword'].encode(), user.password.encode() ):
            request.session['user'] = user.id
            request.session['fname'] = user.first_name
            return redirect('/wall')
        else:
            return render(request, 'wall_app/index.html', {'error': 'Invalid email or password'})

    return render(request, 'wall_app/index.html')


def wall(request):
    if 'user' not in request.session:  # Make sure user is kicked back to index if not in session
        return redirect('/')
    context = {
        'fname': request.session['fname'],
        'messages': Message.objects.all(),
        'comments': Comment.objects.all(),
    }
    return render(request, 'wall_app/wall.html', context)


def post_message(request):
    if request.method == 'POST':
        new_message = Message.objects.create(
            message_text=request.POST['msg'],
            user=User.objects.get(id=request.session['user'])
        )
        new_message.save()
    return redirect('/wall')


def post_comment(request, msg_id):
    if request.method == 'POST':
        new_comment = Comment.objects.create(
            comment_text=request.POST['cmnt'],
            user=User.objects.get(id=request.session['user']),
            message=Message.objects.get(id=msg_id)
        )
        new_comment.save()
    return redirect('/wall')


def logout(request):
    request.session.clear()
    return redirect('/')
