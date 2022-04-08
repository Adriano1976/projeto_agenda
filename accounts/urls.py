from django.urls import path
from . import views

urlpatterns = [
    # /accounts/index_login
    path('', views.login, name='index_login'),
    # /accounts/login
    path('login/', views.login, name='login'),
    # /accounts/logout/
    path('logout/', views.logout, name='logout'),
    # /accounts/register/
    path('register/', views.register, name='register'),
    # /accounts/dashboard/
    path('dashboard/', views.dashboard, name='dashboard'),
    # /accounts/dashboard/




    # ATENçÃO: --- ↑ - Não esquecer da barra!!!
    # Lembre-se que no: djAgPy\agenda\Contatos\urls.py
    # Também deve ter a barra no final.
]
