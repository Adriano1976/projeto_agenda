from django.urls import path
from . import views

# Como exibir nome ao invez da Id na barra de endereços? -----------------------------

app_name = 'contatos'

urlpatterns = [
    # /contato/index
    path('', views.index, name='index'),
    # /contato/busca
    path('busca/', views.busca, name='busca'),
    # /contato/listar_contato
    path('listar_contato', views.listar_contato, name='listar_contato'),
    # /contatos/ver_contato
    path('ver_contato', views.listar_contato, name='ver_contato'),
    # /contatos/id
    path('<int:contato_id>', views.ver_contato, name='ver_contato_id'),  # modifique aqui
]
