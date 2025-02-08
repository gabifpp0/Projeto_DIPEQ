from django import forms
from .models import Empresa, GestaoDePessoas, Redes, Faturamento, FaturamentoMensal
import re, os

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['razaoSocial', 'nomeFantasia', 'cnpj', 'areaAtuacao', 'tempoAtuacaoMercado']

class GestaoDePessoasForm(forms.ModelForm):
    class Meta:
        model = GestaoDePessoas
        fields = ['capitalSocial', 'funcionarioCLT', 'funcionarioTercerizados', 'estagiario', 'numSocios', 'socios']

class RedesForm(forms.ModelForm):
    class Meta:
        model = Redes
        fields = ['website', 'insta', 'facebook', 'twitter', 'linkedin', 'zap', 'email']