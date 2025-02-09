from django.urls import path
from . import views
urlpatterns =[
    path('', views.telaInicial, name='telaInicial'),    
    path('cadastro/', views.cadastroEmpresa, name='cadastroEmpresa'),
    path('cadastro/gestao/', views.gestaoPessoas, name='gestaoPessoas'),
    path('cadastro/redes/', views.cadastroRedes, name='cadastroRedes'),
    path('cadastro/faturamento/', views.faturamento, name='faturamento'),
    path('dashboard/', views.dashboard, name='dashboard'),
]