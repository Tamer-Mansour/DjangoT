import bcrypt
from django.contrib import messages
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from . import forms
from .models import Comment, Message, User


def login(request):
    print("login")
    print(request.method)
    if request.method == "POST":
        print("method was post")
        login_form = forms.Login(request.POST)
        context = dict(login_form=login_form, register_form=forms.Register())
        if login_form.is_valid():
            email = login_form.cleaned_data["email"]
        else:
            messages.error("hmm...something was wrong with your login")
            return redirect(reverse('login'))
        users = User.objects.filter(email=email)
        print("printing users")
        print(users)
        if not users:
            messages.error(request, "This user does not exist")
            return render(request, 'wall_app/login.html', context=context)
        user = users[0]

        password = login_form.cleaned_data["password"]
        if not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
            messages.error(request, "The password is incorrect")
            return render(request, 'wall_app/login.html', context=context)

        messages.success(request, f"Welcome back {user.first_name}!")
        request.session['user_id'] = user.id
        return redirect(to=reverse("index"))

    login_form = forms.Login()
    register_form = forms.Register()
    context = dict(login_form=login_form, register_form=register_form)
    return render(request, "wall_app/login.html", context=context)


def register(request):
    print("register hit")
    if request.method == "POST":
        form = forms.Register(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode(), salt)
            user = User.objects.create(
                email=form.cleaned_data['email'],
                password_hash=password_hash.decode(),
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.save()
            request.session["user_id"] = user.id
            print("register is doing a redirect")
            return redirect(to=reverse('index'))
    else:
        return redirect(to=reverse('login'))


def message(request):
    print("message hit")
    if request.method == "GET":
        return HttpResponse("You can't render message. If you could it would require a pk.")
    if request.method == "POST":
        form = forms.Message(request.POST)
        if form.is_valid():
            m = Message(
                user_id=request.session['user_id'],
                message=form.cleaned_data["message"],
            )
            m.save()
        else:
            return HttpResponse("add message failure logic")
        print("created a messaged, now redirecting to index")
        return redirect("index")


def comment(request):
    if "user_id" not in request.session:
        messages.error("Please sign in")
        return redirect(reverse('login'))

    if request.method != "POST":
        return HttpResponse("Error - Invalid method called")
    else:
        print("hmm what got posted")
        print(request.POST)
        form = forms.Message(request.POST)
        if form.is_valid():

            c = Comment(
                user_id=request.session['user_id'],
                message_id=form.cleaned_data["message"],
                comment=request.POST["comment"]
            )
            c.save()
        else:
            print(form.errors)
            return HttpResponse("Comment failure. Printed form errors to terminal")
        message_user_id = c.message.user.id
        print("message_user_id", message_user_id)
        return redirect(reverse("wall", args=[message_user_id]))


def index(request):
    if 'user_id' not in request.session:
        print("user not logged in, redirecting")
        return redirect(reverse('login'))
    else:
        print("user logged in, redirecting")
        user_id = request.session['user_id']
        return redirect(reverse(wall, args=[user_id]))


def wall(request, user_id):
    if 'user_id' not in request.session:
        return redirect(reverse('login'))
    if request.session["user_id"] == user_id:
        new_message_form = forms.Message()
    else:
        new_message_form = None

    try:
        wall_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404("The requested user does not exist")
    wall_messages = wall_user.message_set.order_by('-created_at')

    for m in wall_messages:
        m.comment_form = forms.Comment()

    context = dict(new_message_form=new_message_form, wall_messages=wall_messages,
                   user_id=request.session["user_id"])

    return render(request, "wall_app/wall.html", context)


def delete_message(request, message_id):
    try:
        m = Message.objects.get(id=message_id)
    except Message.DoesNotExist:
        return Http404("the message does not exist")

    if request.session["user_id"] != m.user.id:
        return HttpResponse("You don't own this message")
    m.delete()
    return redirect(reverse("index"))


def delete_comment(request, comment_id):
    try:
        c = Comment.objects.get(id=comment_id)
    except Message.DoesNotExist:
        return Http404("the comment does not exist")

    if request.session["user_id"] != c.user.id:
        return HttpResponse("You don't own this message")
    wall_user_id = c.message.user.id
    c.delete()
    return redirect(reverse("wall", args=[wall_user_id]))


def logout(request):
    if 'email' in request.session:
        del request.session['email']

    messages.success(request, "Come back soon")
    return redirect(to=reverse('index'))
