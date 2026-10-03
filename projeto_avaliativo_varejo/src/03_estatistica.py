import os

import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("resultados", exist_ok=True)

df = pd.read_csv("data/processed/SuperMarket_processed.csv")
df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce")
df["valor_total"] = pd.to_numeric(df["valor_total"], errors="coerce")
df["avaliacao"] = pd.to_numeric(df["avaliacao"], errors="coerce")


def salvar_grafico(dados, nome_arquivo, titulo, rotacao=0, formato="%.2f"):
	ax = dados.plot(kind="bar", figsize=(10, 6))
	ax.set_title(titulo)
	ax.set_xlabel("")
	ax.tick_params(axis="x", labelrotation=rotacao)
	for container in ax.containers:
		rotulos = [
			"" if pd.isna(barra.get_height()) else formato % barra.get_height()
			for barra in container
		]
		ax.bar_label(container, labels=rotulos, padding=3, fontsize=8)
	ax.margins(y=0.15)
	ax.figure.tight_layout()
	ax.figure.savefig(f"resultados/{nome_arquivo}", dpi=150)
	plt.close(ax.figure)


faturamento_filial = (
	df.groupby("filial")["valor_total"]
	.sum()
	.sort_values(ascending=False)
)
salvar_grafico(
	faturamento_filial,
	"faturamento_por_filial.png",
	"Faturamento total por filial"
)

vendas_filial = df.groupby("filial")["id_venda"].nunique().sort_values(ascending=False)
salvar_grafico(
	vendas_filial,
	"quantidade_vendas_por_filial.png",
	"Quantidade de vendas por filial",
	formato="%.0f"
)

faturamento_linha = (
	df.groupby("linha_produto")["valor_total"]
	.sum()
	.sort_values(ascending=False)
)
salvar_grafico(
	faturamento_linha,
	"faturamento_por_linha_produto.png",
	"Faturamento por linha de produto",
	rotacao=25,
	formato="%.2f"
)

avaliacao_linha = (
	df.groupby("linha_produto")["avaliacao"]
	.mean()
	.sort_values(ascending=False)
)
salvar_grafico(
	avaliacao_linha,
	"avaliacao_media_por_linha_produto.png",
	"Avaliação média por linha de produto",
	rotacao=25
)

pagamentos = df.groupby("forma_pagamento")["id_venda"].nunique().sort_values(
	ascending=False
)
plt.figure(figsize=(8, 8))
plt.pie(
	pagamentos,
	labels=[f"{forma} ({quantidade})" for forma, quantidade in pagamentos.items()],
	autopct="%1.1f%%",
	startangle=90
)
plt.title("Vendas por forma de pagamento")
plt.axis("equal")
plt.tight_layout()
plt.savefig("resultados/uso_por_forma_pagamento.png", dpi=150)
plt.close()

media_mes = df.groupby(df["data_venda"].dt.to_period("M"))["valor_total"].mean()
media_mes.index = media_mes.index.astype(str)
salvar_grafico(
	media_mes,
	"valor_medio_por_mes.png",
	"Valor médio das vendas por mês"
)

top_vendas = df.sort_values("valor_total", ascending=False).groupby("filial").head(3).copy()
top_vendas["posicao"] = top_vendas.groupby("filial").cumcount() + 1
top_vendas_por_filial = top_vendas.pivot(
	index="filial",
	columns="posicao",
	values="valor_total"
).reindex(columns=[1, 2, 3])
top_vendas_por_filial.columns = ["Maior", "2ª maior", "3ª maior"]
salvar_grafico(
	top_vendas_por_filial,
	"tres_maiores_vendas_por_filial.png",
	"Três maiores vendas por filial"
)

nomes_dias = [
	"Segunda-feira",
	"Terça-feira",
	"Quarta-feira",
	"Quinta-feira",
	"Sexta-feira",
	"Sábado",
	"Domingo",
]
media_dia = (
	df.groupby(df["data_venda"].dt.dayofweek)["valor_total"]
	.mean()
	.reindex(range(7))
)
media_dia.index = nomes_dias
salvar_grafico(
	media_dia,
	"valor_medio_por_dia_semana.png",
	"Média das vendas por dia da semana",
	rotacao=25
)