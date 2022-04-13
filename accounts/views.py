from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Contato, FormContato
from accounts.forms import InsereContatoForm

app_name = 'accounts'


# FAZENDO LOGIN DOS USUÁRIOS USANDO "FUNCTION BASED VIEWS"
# ------------------------------------------------------------------------------------

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso.')
        return redirect('contatos:index')


# FAZENDO LOGOUT DOS USUÁRIOS USANDO "FUNCTION BASED VIEWS"
# ------------------------------------------------------------------------------------

def logout(request):
    auth.logout(request)
    return redirect('accounts:login')


# CADASTRANDO OS USUÁRIOS USANDO "FUNCTION BASED VIEWS"
# ------------------------------------------------------------------------------------


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha1 = request.POST.get('senha1')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha1:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'accounts/register.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/register.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/register.html')

    if senha != senha1:
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já existe.')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Cadastro registrado com sucesso! Agora faça login.')

    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome,
                                    last_name=sobrenome)
    user.save()
    return redirect('accounts:login')


# CADASTRANDO OS CONTATOS USANDO "FUNCTION BASED VIEWS"
# ------------------------------------------------------------------------------------


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)
    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    descricao = request.POST.get('descricao')
    if len(descricao) < 5:
        messages.error(request, 'Descrição precisa ter mais que 5 caracteres.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(
        request, f'Contato {request.POST.get("nome")} {request.POST.get("sobrenome")} salvo com sucesso!'
    )
    return redirect('dashboard')


# CADASTRANDO OS CONTATOS USANDO "CLASS BASED VIEWS"
# ------------------------------------------------------------------------------------


class ContatoCreateView(CreateView):
    login_required(redirect_field_name='login')
    template_name = "accounts/register_contact.html"
    model = Contato
    form_class = InsereContatoForm
    success_url = reverse_lazy("contatos:listar_contato")


# ATUALIZANDO OS CONTATOS USANDO "CLASS BASED VIEWS"
# ------------------------------------------------------------------------------------

class ContatoUpdateView(UpdateView):
    login_required(redirect_field_name='login')
    template_name = "accounts/update_contact.html"
    model = Contato
    fields = '__all__'
    context_object_name = 'contato'
    success_url = reverse_lazy("contatos:listar_contato")


# APAGANDO OS CONTATOS USANDO "CLASS BASED VIEWS"
# ------------------------------------------------------------------------------------


class ContatoDeleteView(DeleteView):
    login_required(redirect_field_name='login')
    template_name = "accounts/delete_contact.html"
    model = Contato
    context_object_name = 'contato'
    success_url = reverse_lazy("contatos:listar_contato")
