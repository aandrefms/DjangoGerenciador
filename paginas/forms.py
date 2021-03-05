from django.contrib.auth.forms import UserCreationForm
from .models import Funcionario



class CriarUsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Funcionario
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'setor', 'funcao')

