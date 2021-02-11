# Generated by Django 3.1.5 on 2021-02-11 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='tipo_documento',
            field=models.CharField(default='presencial', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documento',
            name='processo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processo', to='infra.processo'),
        ),
    ]