from django.db import models
from .choices import *
from django.utils.translation import gettext as _
import datetime


class Solicitacao(models.Model):
    tipo_solicitacao = models.CharField(max_length=120, choices=SOLICITACOES)
    turno = models.CharField(max_length=120, choices=TURNO)
    tipo_servico = models.CharField(max_length=120, choices=SERVICOS)
    periodo = models.CharField(max_length=120)
    detalhes = models.CharField(max_length=300)
    local = models.CharField(max_length=300)
