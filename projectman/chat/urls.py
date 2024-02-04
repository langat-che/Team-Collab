from django.urls import path, re_path
from chat import views as chat_views
from . import views


urlpatterns = [
    path("", views.index, name="chat"),
    path("<str:room_name>/", views.room, name="room"),
    path("chats/", chat_views.chatPage, name="chat-page"),
]