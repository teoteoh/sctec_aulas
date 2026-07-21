from array import array

# Criando um array de inteiros (tipo 'i')
numeros = array('i', [10, 20, 30, 40, 50])

print("Array original:", numeros)

# Acessando um elemento pelo índice
print("Elemento no índice 2:", numeros[2])

# Alterando um elemento
numeros[0] = 100
print("Array após alteração:", numeros)

# Adicionando um elemento ao final
numeros.append(60)
print("Array após append:", numeros)

# Removendo um elemento
numeros.remove(30)
print("Array após remover o 30:", numeros)

# Percorrendo o array
print("Percorrendo o array:")
for valor in numeros:
    print(valor)

# Tamanho do array
print("Tamanho do array:", len(numeros))