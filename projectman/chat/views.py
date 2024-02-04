from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
# Create your views here.

def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

from django.shortcuts import render, redirect
 
 
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("teams")
    context = {}
    return render(request, "chat/chatPage.html", context)