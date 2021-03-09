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

        widgets = {'cpf': forms.TextInput(attrs={'data-mask': "000.000.000-00", 'class': 'cpf-rg'}),
                   'situacao_funcional': forms.TextInput(attrs={'class': 'cpf-rg'}),
                   'data_nascimento': forms.TextInput(attrs={'data-mask': "00/00/0000", 'class': 'datatam'}),
                   'nome': forms.TextInput(attrs={'class': 'inputnome'}),
                   'cor': forms.TextInput(attrs={'class': 'datatam'}),
                   'telefone_celular': forms.TextInput(attrs={'data-mask':"(00) 00000-0000" ,'class': 'teltam'}),
                   'telefone_residencial': forms.TextInput(attrs={'data-mask': "(00) 0000-0000", 'class': 'teltam'}),
                   'data_emissao_rg': forms.TextInput(attrs={'data-mask': " 00/00/0000", 'class': 'datatam'}),
                   'uf_rg': forms.TextInput(attrs={'class': 'datatam'}),
                   'nome_mae': forms.TextInput(attrs={'class': 'inputnome'}),
                   'orgao_emissor': forms.TextInput(attrs={'class': 'datatam'}),
                   'naturalidade': forms.TextInput(attrs={'class': 'cpf-rg'}),
                   'cep': forms.TextInput(attrs={'data-mask': "00000-000",'class': 'cpf-rg'}),
                   'bairro': forms.TextInput(attrs={'class': 'bairro'}),
                   'numero': forms.TextInput(attrs={'class': 'datatam'}),
                   'complemento': forms.TextInput(attrs={'class': 'bairro'}),
                   'cidade': forms.TextInput(attrs={'class': 'cpf-rg'}),
                   'endereco': forms.TextInput(attrs={'id': 'endereco'}),
                   'uf': forms.TextInput(attrs={'class': 'datatam'}),
                   'rg': forms.TextInput(attrs={'data-mask': '000.000.000.000-0', 'class': 'cpf-rg'})}



class FuncionarioQueryForm(forms.ModelForm):
    class Meta:
        model = FuncionarioQuery
        fields = '__all__'

