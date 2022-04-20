from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from .models import Contato


# Como exibir nome ao invez da Id na barra de endereços? ------------------------------------

@login_required(redirect_field_name='login')
def index(request):
    return render(request, 'contatos/index.html')


@login_required(redirect_field_name='login')
def listar_contato(request):
    contatos = Contato.objects.order_by('nome').filter(
        mostrar=True,
    )

    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/listar_contato.html', {
        'contatos': contatos,
    })


@login_required(redirect_field_name='login')
def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)  # modifique aqui -------------------

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


@login_required(redirect_field_name='login')
def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo) | Q(categoria__nome__icontains=termo)
    )

    if termo is None or not termo:
        # raise Http404()
        messages.add_message(request, messages.ERROR, 'Campo de busca não pode ficar vazio.')
        return redirect('listar_contato')

    if int(len(contatos)) == 0:
        messages.add_message(request, messages.ERROR, 'Contato(s) não encontrado(s).')
        return redirect('listar_contato')

    if int(len(contatos)) != 0:
        messages.add_message(request, messages.SUCCESS, 'Contato(s) localizado(s) com sucesso.')

        # contatos = Contato.objects.order_by('-id').filter(
        #     Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
        #     mostrar=True
        # )

        paginator = Paginator(contatos, 20)

        page = request.GET.get('p')
        contatos = paginator.get_page(page)

        return render(request, 'contatos/busca.html', {'contatos': contatos})
