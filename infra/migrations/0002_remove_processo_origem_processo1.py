# Generated by Django 3.1.5 on 2021-02-07 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processo',
            name='origem_processo1',
        ),
    ]