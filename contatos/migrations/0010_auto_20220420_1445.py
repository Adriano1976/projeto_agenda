# Generated by Django 3.2.8 on 2022-04-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0009_auto_20220420_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=False, verbose_name='categoria'),
        ),
    ]
