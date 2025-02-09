from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import EmpresaForm, GestaoDePessoasForm, RedesForm, FaturamentoForm, FaturamentoMesForm
from .models import Empresa, GestaoDePessoas, Redes, Faturamento, FaturamentoMensal
from django.utils import timezone
from django.forms import modelformset_factory

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

def cadastroRedes(request):
    empresa_id = request.session.get('empresa_id')
    if not empresa_id:
        return redirect('cadastroEmpresa')
    
    empresa = get_object_or_404(Empresa, id=empresa_id)

    if request.method == 'POST':
        form = RedesForm(request.POST)
        if form.is_valid():
            redes = form.save(commit=False)
            redes.empresa = empresa
            redes.save()
            return redirect('faturamento')
        
    else:
        form = RedesForm()
    return render(request, 'redes.html', {'form': form})

def faturamento(request):
    empresa_id = request.session.get('empresa_id')
    if not empresa_id:
        return redirect('cadastroEmpresa')

    empresa = get_object_or_404(Empresa, id=empresa_id)

    if request.method == 'POST':
        form = FaturamentoForm(request.POST)
        if form.is_valid():
            faturamento = form.save(commit=False)
            faturamento.empresa = empresa
            faturamento.save()

            # Criar automaticamente os faturamentos dos últimos 3 meses do último ano registrado
            meses_atuais = [10, 11, 12]  # Últimos 3 meses (Outubro, Novembro, Dezembro)
            for mes in meses_atuais:
                FaturamentoMensal.objects.create(
                    faturamento=faturamento,
                    mes=mes,
                    valor=0  # O usuário pode atualizar depois
                )

            return redirect('dashboard')

    else:
        form = FaturamentoForm()

    return render(request, 'faturamento.html', {'form': form})


def dashboard(request):
    return render(request,"dashboard.html")