from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import UserAdditionalInfo
from django.utils.translation import ugettext_lazy as _


class UserRegisterForm(UserCreationForm):
    email = forms.CharField(label="",
                            widget=forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': _('Email Address')}))
    username = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': _('Username')}))
    password1 = forms.CharField(label="",
                                widget=forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': _('Password')}))
    password2 = forms.CharField(label="",
                                widget=forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': _('Repeat Password')}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Username'), }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password')}))
