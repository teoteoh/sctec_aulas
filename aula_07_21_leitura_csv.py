import csv

nome_arquivo = "dados.csv"

# 1. Criando um arquivo CSV de exemplo (modo "w")
with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["nome", "idade", "cidade"])
    escritor.writerow(["Ana", "23", "São Paulo"])
    escritor.writerow(["Bruno", "31", "Rio de Janeiro"])
    escritor.writerow(["Carla", "27", "Belo Horizonte"])

print("Arquivo CSV criado!")

# 2. Lendo o CSV e importando os dados para dentro do programa
dados = []
with open(nome_arquivo, "r", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        dados.append(linha)

# 3. Usando os dados já importados
print("\nDados importados do CSV:")
for pessoa in dados:
    print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']} | Cidade: {pessoa['cidade']}")

print(f"\nTotal de registros importados: {len(dados)}")