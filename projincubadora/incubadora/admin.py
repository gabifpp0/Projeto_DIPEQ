from django.contrib import admin
from .models import Empresa, GestaoDePessoas, Redes, Faturamento, FaturamentoMensal

# Register your models here.

admin.site.register(Empresa)
admin.site.register(GestaoDePessoas)
admin.site.register(Redes)
admin.site.register(Faturamento)
admin.site.register(FaturamentoMensal)