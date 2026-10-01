import pandas as pd
from dotenv import dotenv_values
from sqlalchemy import create_engine

caminho_csv = "data/raw/SuperMarket Analysis.csv"

url_supermarket_db = dotenv_values().get("SUPERMARKET_DB_URL")

df_raw = pd.read_csv(
    "../data/raw/SuperMarket Analysis.csv",
    sep=",",
    encoding="utf-8-sig"
)

print("Dimensões:", df_raw.shape)
print(df_raw.head())
df_raw.info()
print("Valores ausentes por coluna:")
print(df_raw.isna().sum())
print("Linhas duplicadas:", df_raw.duplicated().sum())



engine = create_engine(url_supermarket_db)

df_raw.to_sql(
    "raw",
    con=engine,
    schema="public",
    if_exists="replace",
    index=False
)

print("Dados carregados na tabela public.raw.")
engine.dispose()
