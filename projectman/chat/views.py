from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message

def user_selection(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude the current user
    return render(request, 'chat/user_selection.html', {'users': users})

@login_required
def chat_room(request, user_id):
    receiver = User.objects.get(id=user_id)
    form = MessageForm()
    messages_chats_sent = Message.objects.filter(receiver=receiver, sender=request.user) 
    messages_chats_received = Message.objects.filter(receiver=request.user, sender=receiver) 
    messages_chats = messages_chats_sent.union(messages_chats_received)
    print("Message chats: ", messages_chats )
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            sender = request.user
            Message.objects.create(sender=sender, receiver=receiver, content=content)
            return redirect('chat_room', user_id=user_id)

    return render(request, 'chat/chat_room.html', {'receiver': receiver, 'sender': request.user,'form': form, 'messages_chats': messages_chats})