# Generated by Django 3.1.5 on 2021-02-07 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0006_funcionario_cpf2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='cpf2',
        ),
    ]
