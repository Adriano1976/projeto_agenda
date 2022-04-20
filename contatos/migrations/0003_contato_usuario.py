# Generated by Django 3.2.8 on 2022-04-19 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contatos', '0002_auto_20220407_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='usuário'),
        ),
    ]