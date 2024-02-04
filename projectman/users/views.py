from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Team
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import UserRegisterForm, ProfileUpdateForm, UpdateUserForm

  
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'users/signup.html', {'form': form})
      
  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'tasks/home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'users/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
  
def profile(request): 
    return render(request, 'profile.html')
   
def signout(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Successful Logout')
    return redirect('home')


def view_profile(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'profile_view.html', {'profile': profile})


    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


##Profile view
@login_required
def profile(request):
    return render(request, 'registration/profile.html')


##Profile update
# @login_required
# def profile_update_view(request):
#     profile = request.user.profile 
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile was successfully updated!')
#             return redirect('profile')  # Redirect to the user's profile detail page
#     else:
#         form = ProfileUpdateForm(instance=profile)

#     return render(request, 'registration/profile_edit.html', {'form': form})


@login_required
def profile_update_view(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')  # Update with the name of your profile view
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'registration/profile_edit.html', context)


##change password view
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update the user's session to reflect the password change
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'registration/change_password.html', {'form': form})



##Team list view
def teams(request):
    teams = Team.objects.all()
    return render(request, 'registration/team_list.html', {'teams': teams})



##Team members listview
def members(request, team_id):
    team = Team.objects.get(pk=team_id)
    team_users = Profile.objects.filter(team=team)
    return render(request, 'registration/member_list.html', {'team': team, 'team_users': team_users})