from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'college', 'leetcode_id', 'profile_image', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    pass
