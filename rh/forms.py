from django import forms
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        # Preciso colocar quaisquer alterações em Models
        fields = ("situacao_funcional", "nome", "naturalidade", "cor", "nome_mae", "data_nascimento",
                  "foto_3x4", "comprovante_residencia", "rg", "orgao_emissor", "uf_rg",
                  "data_emissao_rg", "endereco", "numero", "complemento", "bairro", "cep",
                  "cidade", "uf", "telefone_residencial", "telefone_celular")
        # fields = '__all__'

