# Generated by Django 3.2.8 on 2022-04-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0011_alter_contato_mostrar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=False),
        ),
    ]