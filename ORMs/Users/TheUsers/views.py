from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Post, Like, Comment


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('/')
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
                return redirect('/')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.bio = request.POST.get('bio')
        profile.gender = request.POST.get('gender')

        image = request.FILES.get('image')
        if image:
            profile.image = image

        profile.save()

    context = {
        'user': request.user,
    }
    return render(request, 'profile.html', context)


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


from django.shortcuts import render, redirect
from .models import Post

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        body = request.POST.get('body')
        request.user.username

        post = Post.objects.create(
            title=title,
            image=image,
            body=body,
            author = request.user
        )

        return redirect('')

    return render(request, 'create_post.html')

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if 'like' in request.POST:
            Like.objects.create(user=request.user, post=post)
        if 'comment' in request.POST:
            body = request.POST.get('body')
            Comment.objects.create(user=request.user, post=post, body=body)
    likes = post.like_set.count()
    comments = post.comment_set.all()
    context = {
        'post': post,
        'likes': likes,
        'comments': comments,
    }
    return render(request, 'post_detail.html', context)

def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts_list.html', context)
