import pandas as pd
from dotenv import dotenv_values
from sqlalchemy import create_engine

caminho_csv = "data/raw/SuperMarket Analysis.csv"

url_supermarket_db = dotenv_values().get("SUPERMARKET_DB_URL")

df_raw = pd.read_csv(
    caminho_csv,
    sep=",",
    encoding="utf-8-sig"
)

df_raw = df_raw.rename(columns={
    "Invoice ID": "invoice_id",
    "Branch": "branch",
    "City": "city",
    "Customer type": "customer_type",
    "Gender": "gender",
    "Product line": "product_line",
    "Unit price": "unit_price",
    "Quantity": "quantity",
    "Tax 5%": "tax_5",
    "Sales": "sales",
    "Date": "sale_date",
    "Time": "sale_time",
    "Payment": "payment",
    "cogs": "cogs",
    "gross margin percentage": "gross_margin_percentage",
    "gross income": "gross_income",
    "Rating": "rating"
})

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