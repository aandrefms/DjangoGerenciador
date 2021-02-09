from django import forms
from .models import Funcionario, FuncionarioQuery
from django.forms import ClearableFileInput

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        # Preciso colocar quaisquer alterações em Models
        fields = '__all__'
        """ fields = ("situacao_funcional", "nome", "naturalidade", "cor", "nome_mae", "data_nascimento",
                   "foto_3x4", "comprovante_residencia", "rg", "orgao_emissor", "uf_rg",
                   "data_emissao_rg", "endereco", "numero", "complemento", "bairro", "cep", 
                   "cidade", "uf", "telefone_residencial", "telefone_celular")"""

        widgets = {'cpf': forms.TextInput(attrs={'data-mask': "000.000.000-00"}),
                   'data_nascimento': forms.TextInput(attrs={'data-mask': "00/00/0000"}),
                   'rg': forms.TextInput(attrs={'data-mask': '000.000.000.000-0'})}



class FuncionarioQueryForm(forms.ModelForm):
    class Meta:
        model = FuncionarioQuery
        fields = '__all__'

