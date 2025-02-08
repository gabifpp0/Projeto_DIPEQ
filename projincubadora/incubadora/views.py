from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import EmpresaForm, GestaoDePessoasForm, RedesForm
from .models import Empresa, GestaoDePessoas, Redes

# Create your views here.

def telaInicial(request):
    return render(request,'home.html')

def cadastroEmpresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save()
            request.session['empresa_id'] = empresa.id
            return redirect('gestaoPessoas')
    else:
        form = EmpresaForm()
    return render(request, 'cadastro.html', {'form': form})

def gestaoPessoas(request):
    empresa_id = request.session.get('empresa_id')
    if not empresa_id:
        return redirect('cadastroEmpresa')
    
    empresa = get_object_or_404(Empresa, id=empresa_id)

    if request.method == 'POST':
        form = GestaoDePessoasForm(request.POST)
        if form.is_valid():
            gestao = form.save(commit=False)
            gestao.empresa = empresa
            gestao.save()
            return redirect('cadastroRedes')
        
    else:
        form = GestaoDePessoasForm()
    return render(request, 'gestao.html', {'form': form})
    #return render(request,"gestao.html")

def cadastroRedes(request):
    empresa_id = request.session.get('empresa_id')
    if not empresa_id:
        return redirect('cadastroEmpresa')
    
    empresa = get_object_or_404(Empresa, id=empresa_id)

    if request.method == 'POST':
        form = RedesForm(request.POST)
        if form.is_valid():
            redes = form.save()
            redes.empresa = empresa
            redes.save()
            del request.session['empresa_id']
            return redirect('dashboard')
        
    else:
        form = RedesForm()
    return render(request, 'redes.html', {'form': form})
    #return render(request,"redes.html")

#def faturamento(request):
    #return render(request,"faturamento.html")

def dashboard(request):
    return render(request,"dashboard.html")