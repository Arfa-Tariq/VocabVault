from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

#extending Django's built-in signup form (UserCreationForm) and telling it to use your custom model: CustomUser
class CustomUserCreationForm(UserCreationForm):
    '''So this form will:
        Validate two matching passwords
        Save the new user into your PostgreSQL DB
        Work with your custom user mode'''
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    class Meta:   #This is a nested class used to tell Django which model and fields to use in the form.
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
