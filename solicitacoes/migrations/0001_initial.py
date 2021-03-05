# Generated by Django 3.1.5 on 2021-03-05 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_solicitacao', models.CharField(choices=[('Manutenção', 'Manutenção'), ('Instalação', 'Instalação')], max_length=120)),
                ('turno', models.CharField(choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno')], max_length=120)),
                ('tipo_servico', models.CharField(choices=[('Elétrico', (('Gerador', 'Gerador'), ('Ponto de Força', 'Ponto de Força'), ('Ponto de iluminação', 'Ponto de iluminação'))), ('Hidráulico', (('Falta de água', 'Falta de água'), ('Limpeza de Reservatório', 'Limpeza de Reservatório'), ('Reparo de Peças', 'Reparo de Peças'), ('Vazamento', 'Vazamento'), ('Desobstrução', 'Desobstrução'))), ('Jardinagem e Controle de Pragas', (('Plantio', 'Plantio'), ('Roçagem', 'Roçagem'), ('Controle de Pragas', 'Controle de Pragas'), ('Sanitização', 'Sanitização'))), ('Refrigeração', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('Refrigeração', (('Split', 'Split'), ('Central', 'Central'))), ('Carpintaria e Marcenaria', (('Infiltração Teto', 'Infiltração Teto'), ('Limpeza Teto', 'Limpeza Teto'), ('Instalação de Calhas', 'Instalação de Calhas'), ('Fabricação/Instalação de Móveis', 'Fabricação/Instalação de Móveis'), ('Instalação/Reparação de Portas e Fechaduras', 'Instalação/Reparação de Portas e Fechaduras'))), ('Serviços Gerais', (('Pintura', 'Pintura'), ('Reparo de Gesso', 'Reparo de Gesso'), ('Serviço em alvenaria/Cerâmimca', 'Serviço em alvenaria/Cerâmimca'), ('Reformas Gerais', 'Reformas Gerais'))), ('Outros', 'Outros')], max_length=120)),
                ('servicos', models.CharField(max_length=120)),
                ('periodo', models.CharField(max_length=120)),
                ('detalhes', models.CharField(max_length=300)),
                ('local', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitacaoSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_solicitacao', models.CharField(blank=True, choices=[('Manutenção', 'Manutenção'), ('Instalação', 'Instalação')], max_length=120)),
                ('turno', models.CharField(blank=True, choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno')], max_length=120)),
                ('servicos', models.CharField(blank=True, max_length=120)),
                ('periodo', models.CharField(blank=True, max_length=120)),
            ],
        ),
    ]
