from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role', 'team', 'bio', 'image']
        
        widgets = {
            'role' : forms.TextInput(attrs={'class':'form-control'}),
            'team' : forms.Select(attrs={"class":"form-select"}),
            'bio': forms.TextInput(attrs={"class":"form-control"}),
        }
        
        def __init__(self, *args, **kwargs):
            super(ProfileUpdateForm, self).__init__(*args, **kwargs)
            self.fields['image'].widget.attrs.update({'class': 'form-control'})
            
     
     
     
class UpdateUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["username",'first_name','last_name','email']
        
        widgets = {
            
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),    
        }
        