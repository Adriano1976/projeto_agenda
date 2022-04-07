from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    # /accounts/index_login
    path('login/', views.login, name='login'),
    # /accounts/login/
    path('logout/', views.logout, name='logout'),
    # /accounts/logout/
    path('register/', views.register, name='register'),
    # /accounts/register/
    path('dashboard/', views.dashboard, name='dashboard'),
    # /accounts/dashboard/

    # ATENçÃO: --- ↑ - Não esquecer da barra!!!
    # Lembre-se que no: djAgPy\agenda\Contatos\urls.py
    # Também deve ter a barra no final.
]
