from django.db import models
from datetime import datetime
import re
from .validators import *


# Create your models here.
class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    situacao_funcional = models.CharField(max_length=40, choices=(('Ativo', 'Ativo'), ('Inativo', 'Inativo')))

    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=120, validators=[verify_cpf])
    # cpf2 = models.IntegerField(validators=[verify_cpf])
    naturalidade = models.CharField(max_length=120)
    cor = models.CharField(max_length=120)
    nome_mae = models.CharField(max_length=120)
    # identificao_unica = models.CharField(max_length=120)
    # matricula_siape = models.CharField(max_length=120)
    data_nascimento = models.CharField(max_length=120)

    foto_3x4 = models.ImageField(upload_to='../static/upload/fotos3x4/', validators=[validate_foto])
    comprovante_residencia = models.FileField(upload_to='../static/upload/comprovantesResidencia/',
                                              validators=[validate_comprovante])
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
    id = models.AutoField(primary_key=True)
    situacao_funcional = models.CharField(max_length=120)

    def __str__(self):
        return self.situacao_funcional