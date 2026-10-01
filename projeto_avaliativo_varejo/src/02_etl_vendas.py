import pandas as pd

df_raw = pd.read_csv(
    "data/raw/SuperMarket Analysis.csv",
    sep=",",
    encoding="utf-8-sig"
)

df_processed = df_raw.rename(columns={
    "Invoice ID": "id_venda",
    "Branch": "filial",
    "City": "cidade",
    "Customer type": "tipo_cliente",
    "Gender": "genero",
    "Product line": "linha_produto",
    "Unit price": "preco_unitario",
    "Quantity": "quantidade",
    "Tax 5%": "imposto",
    "Sales": "valor_total",
    "Date": "data_venda",
    "Time": "hora_venda",
    "Payment": "forma_pagamento",
    "cogs": "custo_mercadoria",
    "gross margin percentage": "margem_percentual",
    "gross income": "receita_bruta",
    "Rating": "avaliacao",
})

for coluna in df_processed.select_dtypes(include=["object", "str"]).columns:
    df_processed[coluna] = df_processed[coluna].str.strip().replace("", pd.NA)

df_processed["id_venda"] = df_processed["id_venda"].str.replace("-", "", regex=False)

df_processed = df_processed.dropna(subset=[
    "id_venda",
    "filial",
    "cidade",
    "linha_produto",
    "forma_pagamento",
])

df_processed = df_processed.drop_duplicates(subset="id_venda")

colunas_numericas = [
    "preco_unitario",
    "quantidade",
    "imposto",
    "valor_total",
    "custo_mercadoria",
    "margem_percentual",
    "receita_bruta",
    "avaliacao",
]

for coluna in colunas_numericas:
    df_processed[coluna] = pd.to_numeric(df_processed[coluna], errors="coerce")

df_processed["data_venda"] = pd.to_datetime(
    df_processed["data_venda"],
    format="%m/%d/%Y",
    errors="coerce"
).dt.date

df_processed["hora_venda"] = pd.to_datetime(
    df_processed["hora_venda"],
    format="%I:%M:%S %p",
    errors="coerce"
).dt.time

df_processed["quantidade"] = df_processed["quantidade"].astype("Int64")

df_processed.to_csv(
    "data/processed/SuperMarket_processed.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Arquivo CSV tratado salvo em data/processed/SuperMarket_processed.csv")
