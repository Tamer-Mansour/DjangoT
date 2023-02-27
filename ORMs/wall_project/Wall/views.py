from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Messages, Comments

@login_required
def wall(request):
    messages = Messages.objects.all()
    return render(request, 'wall.html', {'messages': messages})

@login_required
def add_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        Messages.objects.create(user=request.user, message=message)
        messages.success(request, 'Message added successfully!')
        return redirect('wall')
    return render(request, 'add_message.html')

@login_required
def add_comment(request, message_id):
    if request.method == 'POST':
        message = Messages.objects.get(id=message_id)
        comment = request.POST.get('comment')
        Comments.objects.create(message=message, user=request.user, comment=comment)
        messages.success(request, 'Comment added successfully!')
        return redirect('wall')

@login_required
def delete_message(request, message_id):
    message = Messages.objects.get(id=message_id)
    if request.user == message.user:
        message.delete()
        messages.success(request, 'Message deleted successfully!')
    return redirect('wall')
