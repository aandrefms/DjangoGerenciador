from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
# Create your models here.

# Construir uma função verificadora em algum campo


def verify_cpf(cpf):
    validator = '^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$'
    if re.match(validator, cpf) is None:
        raise ValidationError(
            _('%(value)s nao eh um cpf valido'),
            params={'value': cpf},
        )

class Funcionario(models.Model):
    situacao_funcional = models.CharField(max_length=120)

    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=120, validators=[verify_cpf])
    # cpf2 = models.IntegerField(validators=[verify_cpf])
    naturalidade = models.CharField(max_length=120)
    cor = models.CharField(max_length=120)
    nome_mae = models.CharField(max_length=120)
    # identificao_unica = models.CharField(max_length=120)
    # matricula_siape = models.CharField(max_length=120)
    data_nascimento = models.CharField(max_length=120)

    foto_3x4 = models.ImageField(upload_to='../static/upload/fotos3x4/')
    comprovante_residencia = models.FileField(upload_to='../static/upload/comprovantesResidencia/')

    rg = models.CharField(max_length=120)
    orgao_emissor = models.CharField(max_length=120)
    uf_rg = models.CharField(max_length=120)
    data_emissao_rg = models.CharField(max_length=120)

    endereco = models.CharField(max_length=120)
    numero = models.CharField(max_length=120)
    complemento = models.CharField(max_length=120, blank=True)
    bairro = models.CharField(max_length=120)
    cep = models.CharField(max_length=120)
    cidade = models.CharField(max_length=120)
    uf = models.CharField(max_length=120)
    telefone_residencial = models.CharField(max_length=120, blank=True)
    telefone_celular = models.CharField(max_length=120, blank=True)

    data_cadastro = datetime.today().strftime('%d-%m-%Y')

    # Retorna o 'nome' para identificação no painel admin
    def __str__(self):
        return self.nome

class FuncionarioQuery(models.Model):
    situacao_funcional = models.CharField(max_length=120)

    def __str__(self):
        return self.situacao_funcional