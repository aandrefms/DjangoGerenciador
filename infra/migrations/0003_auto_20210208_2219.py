# Generated by Django 3.1.5 on 2021-02-09 01:19

from django.db import migrations, models
import infra.models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0002_remove_processo_origem_processo1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='documentos',
            field=models.FileField(blank=True, upload_to=infra.models.content_file_name),
        ),
    ]
