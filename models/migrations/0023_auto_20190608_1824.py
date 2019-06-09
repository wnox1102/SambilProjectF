# Generated by Django 2.2.2 on 2019-06-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0022_entradacarro_salidacarro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='abierto',
        ),
        migrations.AddField(
            model_name='entrada',
            name='nombre',
            field=models.CharField(default='Nueva Entrada', max_length=30),
            preserve_default=False,
        ),
    ]
