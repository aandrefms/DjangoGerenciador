from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import *

# Create your models here.

setores = (('Secretária da Saúde', 'Secretária da Saúde'), ('Secretária do Transporte', 'Secretária do Transporte'))


class Funcionario(AbstractUser):
    funcao = models.CharField(max_length=40)
    setor = models.CharField(max_length=100, choices=setores)
    cpf = models.CharField(max_length=120, validators=[verify_cpf])
    fotos_funcionario = models.ImageField(upload_to='../static/upload/fotos_funcionario/', validators=[validate_foto],
                                          blank=True)
    SITUACAO = (('Ativo', 'Ativo'), ('Inativo', 'Inativo') )
    situacao = models.CharField(max_length=40, choices=SITUACAO, default=SITUACAO[0][0])

    is_active = models.BooleanField(default=True, )
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)