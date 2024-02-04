from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from users import views as user_views
from .views import change_password, teams, members,profile_update_view

urlpatterns = [
    path( 'login/', auth_views.LoginView.as_view(), name= 'login'),
    path('logout/',views.signout, name='logout'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path("profile_edit/", user_views.profile_update_view, name= "profile_edit"),
    path('change_password/', change_password, name='change_password'),
    path('teams/', teams, name='teams'),
    path('members/<int:team_id>/', members, name='members'),
]
