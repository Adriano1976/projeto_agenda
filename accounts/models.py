from django import forms
from contatos.models import Contato
from django.contrib.auth.models import User


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar',)

