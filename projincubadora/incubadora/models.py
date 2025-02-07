from django.db import models
from django.core.exceptions import ValidationError

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
        return self.nomeFantasia

class GestaoDePessoas(models.Model):
    capitalSocial = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Capital Social")
    funcionarioCLT = models.IntegerField(verbose_name="Funcionários CLT")
    funcionarioTercerizados = models.IntegerField(verbose_name="Funcionários Terceirizados")
    estagiario = models.IntegerField(verbose_name="Estagiários")
    numSocios = models.IntegerField(verbose_name="Quantidade de Sócios")
    socios = models.CharField(max_length=20, verbose_name="Sócios")

    def __str__(self):
        return self.numSocios

class Redes(models.Model):
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE, related_name="redes")
    website = models.URLField(blank=True, null=True, verbose_name="Website")
    insta = models.URLField(blank=True, null=True, verbose_name="Instagram")
    facebook = models.URLField(blank=True, null=True, verbose_name="Facebook")
    twitter = models.URLField(blank=True, null=True, verbose_name="Twitter")
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    zap = models.CharField(max_length=15, blank=True, null=True, verbose_name="WhatsApp")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

class Faturamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="Empresa")
    ano = models.IntegerField(verbose_name="Ano")
    faturamento = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Faturamento Total Anual")

class FaturamentoMensal(models.Model):
    faturamento = models.ForeignKey(Faturamento, on_delete=models.CASCADE, related_name="Empresa")
    mes = models.IntegerField(verbose_name="Mês", choices=[(i, i) for i in range(1, 13)])
    valor = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Faturamento Mensal")

    def __str__(self):
        return f"Faturamento {self.mes}/{self.faturamento.ano} - {self.faturamento.empresa.nome_fantasia}"