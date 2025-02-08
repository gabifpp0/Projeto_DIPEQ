from django import forms
from .models import Empresa, GestaoDePessoas, Redes, Faturamento, FaturamentoMensal
import re, os

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Empresa, GestaoDePessoas, Redes, 
        fields = ['nome', 'email', 'telefone', 'cargo', 'escolaridade', 'obs', 'arquivo']