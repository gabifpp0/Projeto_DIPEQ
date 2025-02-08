from django.urls import path
from . import views
urlpatterns =[
    path('', views.telaInicial, name='telaInicial'),    
    path('cadastro/', views.cadastroEmpresa, name='cadastroEmpresa'),
    path('cadastro/redes/', views.cadastroRedes, name='cadastroRedes'),
    path('cadastro/gestao/', views.gestaoPessoas, name='gestaoPessoas'),
    path('dashboard/', views.dashboard, name='dashboard'),
]