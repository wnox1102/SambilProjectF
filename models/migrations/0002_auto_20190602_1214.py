# Generated by Django 2.2.1 on 2019-06-02 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EntradaP',
            new_name='EntradaCC',
        ),
        migrations.RenameModel(
            old_name='SalidaP',
            new_name='SalidaCC',
        ),
    ]