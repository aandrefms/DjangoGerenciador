from django.db import models
import uuid
import os
from django.db.models.signals import pre_delete, post_delete
from django.dispatch.dispatcher import receiver


from django.urls import reverse

class Processo(models.Model):
    # unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    origem_processo = models.CharField(max_length=120)
    tipo_processo = models.CharField(max_length=120)
    assunto_detalhado = models.TextField(max_length=900)
    natureza_processo = models.CharField(max_length=120)
    observacao = models.TextField(blank=True)
    documentos = models.FileField(upload_to='../static/upload/pdfs/')
    # imagem = models.ImageField(upload_to='../static/upload/imagens/', null=True, blank=True)

    def __str__(self):
        return self.origem_processo

    def get_absolute_url(self):
        return f"{self.id}/"

    '''def delete(self):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.docfile.name))
'''
'reverse("detalhes_processos", kwargs={"my_id": self.id})'

@receiver(post_delete, sender=Processo)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.documentos.delete(False)