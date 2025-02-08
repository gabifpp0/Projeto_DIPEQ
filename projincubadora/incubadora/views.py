from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def telaInicial(request):
    return render(request, 'home.html')

def cadastroEmpresa(request):
    return render(request,"cadastro.html")

def gestaoPessoas(request):
    return render(request,"gestao.html")

def cadastroRedes(request):
    return render(request,"redes.html")

def dashboard(request):
    return render(request,"dashboard.html")