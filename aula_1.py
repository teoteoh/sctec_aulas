id_venda = input("Digite o ID da Venda: ")
data = input("Digite a Data: ")
vendedor = input("Digite o nome do Vendedor: ")
cliente = input("Digite o nome do Cliente: ")
produto = input("Digite o nome do Produto: ")
categoria = input("Digite a Categoria: ")

quantidade = int(input("Digite a Quantidade: "))

if quantidade > 100:
    print("\nNão temos essa quantidade em estoque!")
else:
    preco_unitario = float(input("Digite o Preço Unitário: R$ "))

    # Calcula o valor total
    valor_total = quantidade * preco_unitario

    # Forma de pagamento
    pagamento = input("Forma de pagamento (À Vista ou A Prazo): ").lower().strip()

    if pagamento == "à vista" or pagamento == "a vista" or pagamento == "avista":
        valor_total *= 0.95  # Desconto de 5%
        forma_pagamento = "À Vista"

    elif pagamento == "a prazo":
        valor_total *= 1.05  # Acréscimo de 5%
        forma_pagamento = "A Prazo"

    else:
        print("Forma de pagamento inválida!")
        forma_pagamento = "Inválida"

    print("\n" + "=" * 40)
    print("            DADOS DA VENDA")
    print("=" * 40)
    print(f"ID da Venda: {id_venda}")
    print(f"Data: {data}")
    print(f"Vendedor: {vendedor}")
    print(f"Cliente: {cliente}")
    print(f"Produto: {produto}")
    print(f"Categoria: {categoria}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço Unitário: R$ {preco_unitario:.2f}")
    print(f"Forma de Pagamento: {forma_pagamento}")
    print(f"Valor Total Atualizado: R$ {valor_total:.2f}")
    print("=" * 40)