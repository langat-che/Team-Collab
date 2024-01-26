from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
  
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
    return redirect('home')


def view_profile(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'profile_view.html', {'profile': profile})

# def image_request(request):  
#     if request.method == 'POST':  
#         form = ProfileForm(request.POST, request.FILES)  
#         if form.is_valid():  
#             form.save()  
  
#             # Getting the current instance object to display in the template  
#             profile_image = form.instance  
              
#             return render(request, 'profile_edit.html', {'form': form, 'profile_image':profile_image})  
#     else:  
#         form = Profile()  
  
#     return render(request, 'profile_edit.html', {'form': form})  

    
# def edit_profile(request):
#     user_profile = Profile.objects.get(user=request.user)

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully!')
#             return redirect('profile_view')
#     else:
#         form = ProfileForm(instance=user_profile)

#     return render(request, 'profile_update.html', {'form': form})



    

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


# Update it here
@login_required
def profile(request):
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST,
    #                                request.FILES,
    #                                instance=request.user.profile)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Your account has been updated!')
    #         return redirect('profile') # Redirect back to profile page

    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     # Check if the user has an associated profile before creating the ProfileUpdateForm
    #     if hasattr(request.user, 'profile'):
    #         p_form = ProfileUpdateForm(instance=request.user.profile)
    #     else:
    #         # If the user does not have a profile, create an empty form
    #         p_form = ProfileUpdateForm()

    # context = {
    #     'u_form': u_form,
    #     'p_form': p_form
    # }

    return render(request, 'registration/profile.html')