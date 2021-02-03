from django.db import models

from django.urls import reverse

# Create your models here.
class Processo(models.Model):
    origem_processo = models.CharField(max_length=120)
    tipo_processo = models.CharField(max_length=120)
    assunto_detalhado = models.TextField(max_length=900)
    natureza_processo = models.CharField(max_length=120)
    observacao = models.TextField(blank=True)

    def get_absolute_url(self):
        return f"{self.id}/"
'reverse("detalhes_processos", kwargs={"my_id": self.id})'
