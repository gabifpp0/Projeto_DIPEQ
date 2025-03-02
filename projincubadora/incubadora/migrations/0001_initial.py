# Generated by Django 5.1.6 on 2025-02-08 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empresa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cnpj",
                    models.CharField(max_length=14, unique=True, verbose_name="CNPJ"),
                ),
                (
                    "razaoSocial",
                    models.CharField(max_length=30, verbose_name="Razão Social"),
                ),
                (
                    "nomeFantasia",
                    models.CharField(max_length=30, verbose_name="Nome Fantasia"),
                ),
                (
                    "areaAtuacao",
                    models.CharField(max_length=30, verbose_name="Área de atuação"),
                ),
                (
                    "tempoAtuacaoMercado",
                    models.IntegerField(verbose_name="Tempo de Atuação no Mercado"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Faturamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.PositiveIntegerField(verbose_name="Ano de referência")),
                (
                    "faturamento",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=15,
                        verbose_name="Faturamento Total Anual",
                    ),
                ),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="faturamentos",
                        to="incubadora.empresa",
                    ),
                ),
            ],
            options={
                "ordering": ["-ano"],
                "unique_together": {("empresa", "ano")},
            },
        ),
        migrations.CreateModel(
            name="GestaoDePessoas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "capitalSocial",
                    models.DecimalField(
                        decimal_places=2, max_digits=15, verbose_name="Capital Social"
                    ),
                ),
                (
                    "funcionarioCLT",
                    models.IntegerField(verbose_name="Funcionários CLT"),
                ),
                (
                    "funcionarioTercerizados",
                    models.IntegerField(verbose_name="Funcionários Terceirizados"),
                ),
                ("estagiario", models.IntegerField(verbose_name="Estagiários")),
                ("numSocios", models.IntegerField(verbose_name="Quantidade de Sócios")),
                ("socios", models.CharField(max_length=20, verbose_name="Sócios")),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gestao_pessoas",
                        to="incubadora.empresa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Redes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="Website"),
                ),
                (
                    "insta",
                    models.URLField(blank=True, null=True, verbose_name="Instagram"),
                ),
                (
                    "facebook",
                    models.URLField(blank=True, null=True, verbose_name="Facebook"),
                ),
                (
                    "twitter",
                    models.URLField(blank=True, null=True, verbose_name="Twitter"),
                ),
                (
                    "linkedin",
                    models.URLField(blank=True, null=True, verbose_name="LinkedIn"),
                ),
                (
                    "zap",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="WhatsApp"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "empresa",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="redes",
                        to="incubadora.empresa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FaturamentoMensal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mes",
                    models.IntegerField(
                        choices=[
                            (1, "Janeiro"),
                            (2, "Fevereiro"),
                            (3, "Março"),
                            (4, "Abril"),
                            (5, "Maio"),
                            (6, "Junho"),
                            (7, "Julho"),
                            (8, "Agosto"),
                            (9, "Setembro"),
                            (10, "Outubro"),
                            (11, "Novembro"),
                            (12, "Dezembro"),
                        ],
                        verbose_name="Mês de referência",
                    ),
                ),
                (
                    "valor",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=15,
                        verbose_name="Faturamento Mensal",
                    ),
                ),
                (
                    "faturamento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="faturamentos_mensais",
                        to="incubadora.faturamento",
                    ),
                ),
            ],
            options={
                "ordering": ["-faturamento__ano", "-mes"],
                "unique_together": {("faturamento", "mes")},
            },
        ),
    ]
