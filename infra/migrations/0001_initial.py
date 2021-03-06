# Generated by Django 3.1.5 on 2021-03-09 04:03

from django.db import migrations, models
import infra.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(max_length=120)),
                ('unique_documento_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('file', models.FileField(blank=True, upload_to='../static/upload/%Y/%m/%d/', validators=[infra.models.validate_pdf])),
            ],
        ),
        migrations.CreateModel(
            name='FilterProcesso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=120)),
                ('tipo_processo', models.CharField(blank=True, max_length=120)),
                ('responsavel', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('origem_processo', models.CharField(max_length=40)),
                ('tipo_processo', models.CharField(choices=[('Abandono de Cargo', 'Abandono de Cargo'), ('Abono de Faltas', 'Abono de Faltas'), ('Abono Permanência', 'Abono Permanência'), ('Ação', 'Ação'), ('Ação Cautelar', 'Ação Cautelar'), ('Ação Civil Púbica', 'Ação Ci vil Púbica'), ('Ação de Indenização', 'Ação de Indenização'), ('Acórdão', 'Acórdão'), ('Acordo', 'Acordo'), ('Adicional', 'Adicional'), ('Aditivo', 'Aditivo'), ('Afastamento', 'Afastamento'), ('Ajuda de Custo', 'Ajuda de Custo'), ('Alienação', 'Alienação'), ('Alteração', 'Alteração'), ('Anulação de Empenho', 'Anulação de Empenho'), ('Aposentadoria', 'Aposentadoria'), ('Auxílio', 'Auxílio'), ('Averbação', 'Averbação'), ('Cancelamento', 'Cancelamento'), ('Certidão', 'Certidão'), ('Cessão', 'Cessão'), ('Cessão de Servidor', 'Cessão de Servidor'), ('Chamada Pública', 'Chamada Pública'), ('Colaboração', 'Colaboração'), ('Comunicação', 'Comunicação'), ('Concorrência', 'Concorrência'), ('Concurso Público', 'Concurso Público'), ('Consulta', 'Consulta'), ('Contratação', 'Contratação'), ('Contrato', 'Contrato'), ('Convênio', 'Convênio'), ('Convite', 'Convite'), ('Credenciamento', 'Credenciamento'), ('Curso', 'Curso'), ('Decisão Judicial', 'Decisão Judicial'), ('Demissão', 'Demissão'), ('Denuncia', 'Denuncia'), ('Designação', 'Designação'), ('Desligamento', 'Desligamento'), ('Diárias', 'Diárias'), ('Diligência', 'Diligência'), ('Dispensa', 'Dispensa'), ('Dispensa de Servidor', 'Dispensa de Servidor'), ('Doação', 'Doação'), ('Emissão', 'Emissão'), ('Emissão de Empenho', 'Emissão de Empenho'), ('Emissão de Portaria', 'Emissão de Portaria'), ('Enquadramento', 'Enquadramento'), ('Estágio Probatório', 'Estágio Probatório'), ('Exercício', 'Exercício'), ('Exoneração', 'Exoneração'), ('Expedição de Documento', 'Expedição de Documento'), ('Expedição de Certidão', 'Expedição de Certidão'), ('Extinção', 'Extinção'), ('Férias', 'Férias'), ('FGTS', 'FGTS'), ('Fiscalização', 'Fiscalização'), ('Frequência', 'Frequência'), ('Gratificação', 'Gratificação'), ('Homologação', 'Homologação'), ('Hospedagem', 'Hospedagem'), ('Incentivo', 'Incentivo'), ('Inclusão', 'Inclusão'), ('Indenização', 'Indenização'), ('Inexigibilidade de Licitação', 'Inexigibilidade de Licitação'), ('Inscrição', 'Inscrição'), ('Isenção', 'Isenção'), ('Justificativa', 'Justificativa'), ('Licença', 'Licença'), ('Licitação', 'Licitação'), ('Mandado de Segurança', 'Mandado de Segurança'), ('Mudança', 'Mudança'), ('Nomeação', 'Nomeação'), ('Notificação', 'Notificação'), ('Pagamento', 'Pagamento'), ('Passagem', 'Passagem'), ('Pedido ', 'Pedido '), ('Penalidade', 'Penalidade'), ('Pensão', 'Pensão'), ('Planejamento', 'Planejamento'), ('Posse', 'Posse'), ('Pregão', 'Pregão'), ('Prestação de Contas', 'Prestação de Contas'), ('Prestação de Serviço', 'Prestação de Serviço'), ('Processo Administrativo – PAD', 'Processo Administrativo – PAD'), ('Processo Seletivo', 'Processo Seletivo'), ('Proposta', 'Proposta'), ('Prorrogação', 'Prorrogação'), ('Providência', 'Providência'), ('Readaptação', 'Readaptação'), ('Reavaliação', 'Reavaliação'), ('Recebimento', 'Recebimento'), ('Reclamação', 'Reclamação'), ('Recondução', 'Recondução'), ('Reconsideração', 'Reconsideração'), ('Recurso', 'Recurso'), ('Redistribuição', 'Redistribuição'), ('Registro', 'Registro'), ('Reintegração', 'Reintegração'), ('Relatório', 'Relatório'), ('Relotação', 'Relotação'), ('Remoção', 'Remoção'), ('Renúncia ', 'Renúncia '), ('Requisição', 'Requisição'), ('Rescisão', 'Rescisão'), ('Ressarcimento', 'Ressarcimento'), ('Resultado', 'Resultado'), ('Retificação', 'Retificação'), ('Revisão', 'Revisão'), ('Reversão', 'Reversão'), ('Sindicância', 'Sindicância'), ('Solicitação', 'Solicitação'), ('Termo Aditivo', 'Termo Aditivo'), ('Tomada de Preço', 'Tomada de Preço'), ('Vacância', 'Vacância')], max_length=40)),
                ('assunto_detalhado', models.CharField(max_length=40)),
                ('observacao', models.CharField(blank=True, max_length=40)),
                ('recebimento', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secretaria', models.CharField(max_length=120)),
            ],
        ),
    ]
