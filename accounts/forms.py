from contatos.models import Contato
from django import forms


# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class InsereContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('usuario',)

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario')
        super(InsereContatoForm, self).__init__(*args, **kwargs)

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False
    )
    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    # Campos que estarão no form
    fields = [
        'nome',
        'sobrenome',
        'telefone',
        'email',
        'data_criacao',
        'descricao',
        'categoria',
        'mostrar',
    ]
