from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class Empresa(models.Model):
    cnpj = models.CharField(max_length=14, unique=True, verbose_name="CNPJ")
    razaoSocial = models.CharField(max_length=30, verbose_name="Razão Social")
    nomeFantasia = models.CharField(max_length=30, verbose_name="Nome Fantasia")
    areaAtuacao = models.CharField(max_length=30, verbose_name="Área de atuação")
    tempoAtuacaoMercado = models.IntegerField(verbose_name="Tempo de Atuação no Mercado")

    def clean(self):
        #Validação do CNPJ
        if not self.cnpj.isdigit():
            raise ValidationError('O CNPJ deve conter apenas números.')
        if len(self.cnpj) != 14:
            raise ValidationError('O CNPJ deve ter 14 dígitos.')
        if Empresa.objects.filter(cnpj=self.cnpj).exclude(pk=self.pk).exists():
                raise ValidationError({'cnpj': ("Já existe um cadastro com esse CNPJ.")})
    def __str__(self):
       
        return self.nomeFantasia if self.nomeFantasia else "Empresa sem nome"

class GestaoDePessoas(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="gestao_pessoas") 
    capitalSocial = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Capital Social")
    funcionarioCLT = models.IntegerField(verbose_name="Funcionários CLT")
    funcionarioTercerizados = models.IntegerField(verbose_name="Funcionários Terceirizados")
    estagiario = models.IntegerField(verbose_name="Estagiários")
    numSocios = models.IntegerField(verbose_name="Quantidade de Sócios")
    socios = models.CharField(max_length=20, verbose_name="Sócios")

    def __str__(self):
        
        return self.socios if self.socios else "Gestão de Pessoas sem Sócios"

class Redes(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="redes", null=True)
    website = models.URLField(blank=True, null=True, verbose_name="Website")
    insta = models.URLField(blank=True, null=True, verbose_name="Instagram")
    facebook = models.URLField(blank=True, null=True, verbose_name="Facebook")
    twitter = models.URLField(blank=True, null=True, verbose_name="Twitter")
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    zap = models.CharField(max_length=15, blank=True, null=True, verbose_name="WhatsApp")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

    def __str__(self):
        
        return self.email if self.email else "Redes sem Email"

class Faturamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="faturamentos")
    ano = models.PositiveIntegerField(verbose_name="Ano de referência")
    faturamento = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Faturamento Total Anual")

    class Meta:
        unique_together = ['empresa', 'ano']
        ordering = ['-ano']

    def __str__(self):
        
        return f"{self.empresa.nomeFantasia if self.empresa else 'Empresa Desconhecida'} - {self.ano}"

class FaturamentoMensal(models.Model):
    meses = [
        (1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'),
        (4, 'Abril'), (5, 'Maio'), (6, 'Junho'),
        (7, 'Julho'), (8, 'Agosto'), (9, 'Setembro'),
        (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro')
    ]
    
    faturamento = models.ForeignKey(Faturamento, on_delete=models.CASCADE, related_name="faturamentos_mensais")
    mes = models.IntegerField(verbose_name="Mês de referência", choices=meses)
    valor = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Faturamento Mensal")

    class Meta:
        unique_together = ['faturamento', 'mes']  
        ordering = ['-faturamento', '-mes'] 

    def __str__(self):
        return f"Faturamento {self.mes}/{self.faturamento.ano} - {self.faturamento.empresa.nomeFantasia if self.faturamento and self.faturamento.empresa else 'Empresa Desconhecida'}"