# Generated by Django 3.1.5 on 2021-03-08 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='situacao',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], default='Ativo', max_length=40),
        ),
    ]
