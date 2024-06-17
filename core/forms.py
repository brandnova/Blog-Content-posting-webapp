from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Todo, Review, Messages

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'role', 'comment', 'image',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'aria-label': 'form-control',
            }),

            'role': forms.TextInput(attrs={
                'class': 'form-control',
                'aria-label': 'form-control',
            }),

            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'aria-label': 'With textarea',
            }),

            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'customFile',
                'label': 'Select an Image (optional)',
            }),
            
        }


class TodoForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    content = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Add Todo...',
        'id': 'content',
        'aria-label': 'form-control',
        'autocomplete': 'off',
    }))

    tag = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'tag',
        'aria-label': 'form-control',
    }))

    class Meta:
        model = Todo
        fields = ('content', 'tag')
       
        


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'Username',
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'Password',
    }))



class CustomUserCreationForm(UserCreationForm):
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

    # Adding password fields with 'required' attribute and max length
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'registerPassword',
    }))

    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'registerRepeatPassword',
    }))

    class Meta:
        model = User  # Assuming User is your custom User model
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')



class MessagesForm(forms.ModelForm):
    # Adding custom attributes to the username field
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'placeholder': 'Your Name'

    }))

    # Adding email field with 'required' attribute
    email = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'placeholder': 'Your Email.'

    }))

    # Adding first_name field with 'required' attribute and max length
    subject = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'subject',
        'placeholder': 'Subject.'

    }))

    # Adding last_name field with 'required' attribute and max length
    message = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'message',
        'placeholder': 'Your message here...'
    }))

    class Meta:
        model = Messages  # Assuming User is your custom User model
        fields = ('name', 'email', 'subject', 'message')
