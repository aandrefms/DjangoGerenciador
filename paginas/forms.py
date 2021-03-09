from django.contrib.auth.forms import UserCreationForm
from .models import Funcionario
from django import forms


class CriarUsuarioForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Funcionario

        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'password1', 'password2',
                                                 'setor', 'funcao', 'cpf', 'fotos_funcionario', 'situacao')

        widgets = {'cpf': forms.TextInput(attrs={'data-mask': "000.000.000-00", 'placeholder': "000.000.000-00"})}
