from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Funcionario(AbstractUser):
    funcao = models.CharField(max_length=40)
    setor = models.CharField(max_length=40)

    is_active = models.BooleanField(default=True, )
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)