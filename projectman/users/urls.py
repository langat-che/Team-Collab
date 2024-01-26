from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from users import views as user_views

urlpatterns = [
    path( 'login/', auth_views.LoginView.as_view(), name= 'login'),
    path('logout/',views.signout, name='logout'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
]
