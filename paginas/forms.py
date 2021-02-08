from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CriarUsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=40, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=40, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

