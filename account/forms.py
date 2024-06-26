from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=70,help_text='Required.Add a valid email address')

    class Meta:
        model = Account
        fields = ("email", "username", "password", "password2"))
