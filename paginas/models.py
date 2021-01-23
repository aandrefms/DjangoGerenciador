from django.db import models


# Create your models here.
class Insumo(models.Model):
    nome = models.TextField(max_length=110)
    categoria = models.TextField()
    quantidade = models.IntegerField()
