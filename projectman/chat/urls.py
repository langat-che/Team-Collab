from django.urls import path, include
from chat import views as chat_views
from . import views
urlpatterns = [
    path('', views.user_selection, name='user_selection'),
    path('chat/<int:user_id>/', views.chat_room, name='chat_room'),
]