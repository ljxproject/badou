from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.views import login
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['mobile']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['mobile', 'password']
