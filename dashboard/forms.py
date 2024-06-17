from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'about',
    }))

    country = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={  # Changed to CharField
        'class': 'form-control',
        'id': 'Country',
    }))

    phone = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'Phone',
    }))

    address = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
    }))

    job = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'job',
    }))

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={  # Set required=False if the image is optional
        'class': 'form-control',
        'id': 'customFile',
    }))

    class Meta:
        model = Profile
        fields = ('bio', 'country', 'phone', 'address', 'job', 'image',)

    
class UserForm(forms.ModelForm):
    # Adding custom attributes to the username field
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'registerUsername',
    }))

    # Adding email field with 'required' attribute
    email = forms.EmailField(max_length=30, required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'registerEmail',
    }))

    # Adding first_name field with 'required' attribute and max length
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'registerName',
    }))

    # Adding last_name field with 'required' attribute and max length
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'registerName',
    }))

    class Meta:
        model = User  # Assuming User is your custom User model
        fields = ('username', 'email', 'first_name', 'last_name')

