from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmpresaForm, GestaoDePessoasForm, RedesForm, FaturamentoForm, FaturamentoMesForm
from .models import Empresa, GestaoDePessoas, Redes, Faturamento, FaturamentoMensal
from django.db.models import Sum

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
        
        anos = [2022, 2023, 2024]
        for ano in anos:
            faturamento_valor = request.POST.get(f'faturamento_{ano}')
            if faturamento_valor:
               
                faturamento, created = Faturamento.objects.get_or_create(
                    empresa=empresa,
                    ano=ano,
                    defaults={'faturamento': faturamento_valor}
                )

                if not created:
                    faturamento.faturamento = faturamento_valor
                    faturamento.save()

                if ano == 2024:
                    meses_atuais = [10, 11, 12] 
                    for mes in meses_atuais:
                        
                        FaturamentoMensal.objects.create(
                            faturamento=faturamento,
                            mes=mes,
                            valor=0 
                        )

        return redirect('sucesso')  

    return render(request, 'faturamento.html')

def dashboard(request):
    
    empresas = Empresa.objects.all()

    
    total_funcionarios = 0
    total_faturamento_ultimo_ano = 0
    total_empresas = empresas.count()  

   
    empresas_com_faturamento_baixo = Empresa.objects.annotate(faturamento_total=Sum('faturamentos__faturamento')).filter(faturamento_total__lt=50000)

    
    for empresa in empresas:
       
        gestao = empresa.gestao_pessoas.first()  
        
        if gestao:
            total_funcionarios += (gestao.funcionarioCLT + gestao.funcionarioTercerizados + gestao.estagiario)

        
        ultimo_faturamento = Faturamento.objects.filter(empresa=empresa).order_by('-ano').first()

        if ultimo_faturamento:
            total_faturamento_ultimo_ano += ultimo_faturamento.faturamento

   
    return render(request, 'dashboard.html', {
        'total_funcionarios': total_funcionarios,
        'total_faturamento_ultimo_ano': total_faturamento_ultimo_ano,
        'total_empresas': total_empresas, 
        'empresas_com_faturamento_baixo': empresas_com_faturamento_baixo,
        'empresas': empresas
    })

def sucesso(request):
    return render(request, 'sucesso.html')