 

Projeto de leitura e processamento de dados de um arquivo CSV com PostgreSQL e python. Utilizados pandas, sqlalchemy, psycopg2-binary, python-dotenv e matplotlib.

# Requisitos

- Python 3
- PostgreSQL
- VS Code com SQLTools e o driver PostgreSQL, ou DBeaver para executar os scripts SQL

## 1. Instalação dos requesitos

Execute na pasta principal através do terminal:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Vai gerar um ambiente virtual e instalar os requisitos.

# 2. Conexão com PostgreSQL

Com base no arquivo env.example, crie um arquivo .env substuinto SENHA pela senha do seu banco de dados PostgreSQL.

## 3. Criando o banco de dados

Através da extensão SQLTools do VSCode ou DBeaver, conecte-se ao banco postgres e siga as etapas seguintes:

1. Execute o que está em **01_criar_banco.sql**. Isso criará o banco de dados supermarket_db, onde estarão as tabelas do projeto.
2. Conecte-se ao banco **supermarket_db**.
3. Execute **sql_02_criar_tabelas** para criar a tabela **processed**.

## 4. Extraindo o CSV e primeiras inspeções

Execute no terminal:

```powershell
.\.venv\Scripts\python.exe .\src\01_leitura_dados.py
```

O script faz uma leitura inicial do arquivo como um dataframe através do pandas, após isso gera a tabela SQL **raw** baseada no dataframe, que é salva na base de dados **supermarket_db**.

## 5. Tratamento de dados

Execute no terminal:

```powershell
.\.venv\Scripts\python.exe .\src\02_etl_vendas.py
```

O ETL faz o tratamento dos dados e o resultado é salvo como csv em **data/processed/SuperMarket_processed.csv** e na tabela **processed**.

## 6. Consulta de dados

Em **sql\03_consultas.sql**, há scripts de consulta de dados criados a partir das perguntas a seguir:

> ●       Qual filial apresentou o maior faturamento?
>
> ●       Qual filial realizou a maior quantidade de vendas?
>
> ●       Qual linha de produto apresentou o maior faturamento?
>
> ●       Qual linha de produto recebeu a melhor avaliação média?
>
> ●       Qual foi a forma de pagamento mais utilizada?
>
> ●       Qual foi o valor médio das vendas?
>
> ●       Qual foi a maior venda registrada?
>
> ●       Em qual dia da semana ocorreu a maior quantidade de vendas?

Execute os scripts através do SQLTools ou DBeaver para ver os resultados.

## 7. Gráficos com matplotlib

Para criar gráficos relacionados às perguntas e dados da tabela, execute o script de **src\03_estatistica.py:**

```powershell
.\.venv\Scripts\python.exe .\src\03_estatistica.py
```

O script cria a pasta **resultados** e salva nela gráficos criados através do matplotlib como arquivos PNG para o usuário visualizar.
