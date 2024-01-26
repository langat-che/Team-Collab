from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['user', 'image', 'bio']       
        
        widgets = {
            'user' : forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.ImageField(),
            'bio': forms.TextInput(attrs={'class':'form-control'}),
        }
        
        # def __init__(self, user=None, *args, **kwargs):
        #     super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        #     self.user = user

        #     # If a user is provided, limit queryset for user field
        #     if user:
        #         self.fields['user'].queryset = User.objects.filter(pk=user.pk)

        def save(self, commit=True):
            instance = super(ProfileUpdateForm, self).save(commit=False)

            if self.user:
                instance.user = self.user

            if commit:
                instance.save()

            return instance