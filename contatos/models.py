import requests
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    objects = None
    nome = models.CharField(max_length=255, verbose_name='nome')
    sobrenome = models.CharField(max_length=255, blank=True, verbose_name='sobrenome')
    telefone = models.CharField(max_length=255, verbose_name='telefone')
    email = models.CharField(max_length=255, blank=True, verbose_name='e-mail')
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name='data de criação')
    descricao = models.TextField(blank=True, verbose_name='descrição')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True, blank=False)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, default=True)

    def __str__(self):
        return self.nome
