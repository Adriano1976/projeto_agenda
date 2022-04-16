from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import ContatoCreateView, ContatoUpdateView, ContatoDeleteView
from accounts import views

app_name = 'accounts'

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
    # /accounts/recover/
    path('recover/', views.recover, name='recover'),

    # GET /accounts/register_contatct/
    path('register_contact/', ContatoCreateView.as_view(), name="register_contact"),
    # GET /POST/contato/{pk}
    path('contato/<pk>', ContatoUpdateView.as_view(), name="update_contact"),
    # GET /POST/contato/delete/{pk}
    path('contato/delete/<pk>', ContatoDeleteView.as_view(), name="delete_contact"),


    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # ATENçÃO: --- ↑ - Não esquecer da barra!!!
    # Lembre-se que no: djAgPy\agenda\Contatos\urls.py
    # Também deve ter a barra no final.
]
