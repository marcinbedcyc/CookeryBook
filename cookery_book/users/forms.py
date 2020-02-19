from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from .models import AdditionalInfo
from django.utils.translation import ugettext_lazy as _


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label=(_("Email address")), required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
