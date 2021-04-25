from django.db import models
import uuid
import os
from django.db.models.signals import pre_delete, post_delete
from django.dispatch.dispatcher import receiver
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.conf import settings
from .choices import *

from django.urls import reverse


def validate_pdf(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Por favor, insira um arquivo com  extensão pdf')


def content_file_name(instance, filename):
    return "../static/upload/pdfs/{folder}/{file}".format(id=instance, folder='2', file=filename)


class Setor(models.Model):
    secretaria = models.CharField(max_length=120)

    def __str__(self):
        return self.secretaria


class Processo(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    origem_processo = models.CharField(max_length=40)
    tipo_processo = models.CharField(max_length=40, choices=TIPO_PROCESSO)
    assunto_detalhado = models.CharField(max_length=40)
    #natureza_processo = models.CharField(max_length=40, choices=NATUREZA_PROCESSO, default=NATUREZA_PROCESSO[0][0])
    observacao = models.CharField(max_length=40, blank=True)
    # documentos = models.FileField(upload_to='../static/upload/pdfs/', blank=True)
    # documentos = models.FileField(upload_to=content_file_name, blank=True)
    # imagem = models.ImageField(upload_to='../static/upload/imagens/', null=True, blank=True)
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET('Sem responsavel'),
                                    related_name='responsavel')

    secretaria = models.ForeignKey(Setor, related_name='setor', on_delete=models.SET_NULL, null=True)
    recebimento = models.BooleanField(default=False)

    # Isto serve para ver o nome 'origem_processo' no admin painel
    def __str__(self):
        return self.origem_processo


class Documento(models.Model):
    tipo_documento = models.CharField(max_length=120)
    unique_documento_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    file = models.FileField(upload_to='../static/upload/%Y/%m/%d/', blank=True, validators=[validate_pdf])
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, related_name='processo'
                                 )


ACAO_PROCESSO = (('Enviar', 'Enviar'), ('Receber', 'Receber'))
class DespatchReceive(models.Model):
    acao_processo = models.CharField(max_length=40, choices=ACAO_PROCESSO)
    status_processo = models.CharField(max_length=40, blank=True, default='False')
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, related_name='status_procesos')
    secretaria = models.ForeignKey(Setor, on_delete=models.CASCADE, related_name='status_setor')


class FilterProcesso(models.Model):
    unique_id = models.CharField(max_length=120, blank=True)
    tipo_processo = models.CharField(max_length=120, blank=True)
    responsavel = models.CharField(max_length=120, blank=True)


@receiver(post_delete, sender=Processo)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.documentos.delete(False)




# Estava em class Processo
    '''def delete(self):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.docfile.name))
'''
'reverse("detalhes_processos", kwargs={"my_id": self.id})'

# asdadasdaaunique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

'''def get_absolute_url(self):
    return f"{self.id}/"'''