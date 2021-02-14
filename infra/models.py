from django.db import models
import uuid
import os
from django.db.models.signals import pre_delete, post_delete
from django.dispatch.dispatcher import receiver
from django.core.exceptions import ValidationError



def validate_pdf(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

from django.urls import reverse
def content_file_name(instance, filename):
    return "../static/upload/pdfs/{folder}/{file}".format(id=instance, folder='2', file=filename)


class Processo(models.Model):
    NATUREZA_PROCESSO = (('OSTENSIVO', 'OSTENSIVO'), ('RESTRITO', 'RESTRITO'))
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    origem_processo = models.CharField(max_length=120)
    tipo_processo = models.CharField(max_length=120)
    assunto_detalhado = models.TextField(max_length=900)
    natureza_processo = models.CharField(max_length=120, choices=NATUREZA_PROCESSO, default=NATUREZA_PROCESSO[0][0])
    observacao = models.TextField(blank=True)
    # documentos = models.FileField(upload_to='../static/upload/pdfs/', blank=True)
    # documentos = models.FileField(upload_to=content_file_name, blank=True)
    # imagem = models.ImageField(upload_to='../static/upload/imagens/', null=True, blank=True)

    # Isto serve para ver o nome 'origem_processo' no admin painel
    def __str__(self):
        return self.origem_processo


class Documento(models.Model):
    tipo_documento = models.CharField(max_length=120)
    unique_documento_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    file = models.FileField(upload_to='../static/upload/%Y/%m/%d/', blank=True)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, related_name='processo',
                                 validators=[validate_pdf])



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