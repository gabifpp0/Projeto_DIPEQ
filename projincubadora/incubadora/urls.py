from django.urls import path
from . import views
urlpatterns =[
    path('', views.telaInicial, name='telaInicial'),
    path('cadastro/', views.cadastroEmpresa, name='cadastroEmpresa'),
    path('redes/', views.cadastroRedes, name='cadastroRedes'),
    path('gestao/', views.gestaoPessoas, name='gestaoPessoas'),
    path('dashboard/', views.gestaoPessoas, name='dashboard'),
]