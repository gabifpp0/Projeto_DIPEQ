from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def telaInicial(self):
    return HttpResponse("Tela inicial")

def cadastroEmpresa(self):
    return HttpResponse("Cadastro da empresa")

def gestaoPessoas(self):
    return HttpResponse("Cadastro de gestão de pessoas")

def cadastroRedes(self):
    return HttpResponse("Cadastro das Redes")

def dashboard(self):
    return HttpResponse("Dashboard")