# Generated by Django 2.2.1 on 2019-06-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0017_auto_20190602_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='macadd',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
