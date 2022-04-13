from contatos.models import Contato, Categoria
from django import forms


# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class InsereContatoForm(forms.ModelForm):
    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Contato

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'telefone',
            'email',
            'data_criacao',
            'descricao',
            'categoria',
        ]
