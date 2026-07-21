nome_arquivo = "frutas.txt"

# 1. Escrevendo em um arquivo (modo "w")
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("maçã\n")
    arquivo.write("banana\n")
    arquivo.write("uva\n")

print("Arquivo criado e preenchido!")

# 2. Adicionando mais conteúdo sem apagar o que já existe (modo "a")
with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
    arquivo.write("pera\n")

print("Nova fruta adicionada ao arquivo!")

# 3. Lendo todo o conteúdo do arquivo (modo "r")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print("\nConteúdo completo do arquivo:")
print(conteudo)

# 4. Lendo o arquivo linha por linha
print("Lendo linha por linha:")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print("Fruta:", linha.strip())  # strip() remove o \n do final