# Generated by Django 3.1.5 on 2021-02-14 20:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('infra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='responsavel',
            field=models.ForeignKey(on_delete=models.SET('Sem responsavel'), related_name='responsavel', to=settings.AUTH_USER_MODEL),
        ),
    ]
