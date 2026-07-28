import csv
from datetime import datetime
import matplotlib.pyplot as plt

saldo = 100
extrato = []
ARQUIVO_CSV = "extrato_movimentacao.csv"

def salvar_no_csv(tipo, valor):
    with open(ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([datetime.now().strftime("%d/%m/%Y %H:%M:%S"), tipo, f"{valor:.2f}", f"{saldo:.2f}"])

def exibir_banco():
    print("\n===== CAIXA ELETRONICO =====")
    print("1- Consultar Saldo")
    print("2- Depositar Dinheiro")
    print("3- Sacar Dinheiro")
    print("4- Ver Extrato")
    print("5- Ver Movimentacao")
    print("6- Sair")

def consultar_saldo():
    print(f"\nSeu saldo atual é: R$ {saldo}")
    pass

def depositar_dinheiro():
    global saldo
    valor = float(input("\nDigite o valor a ser depositado R$ "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        salvar_no_csv("Depósito", valor)
        print(f"\nDeposito de R$ {valor} realizado com sucesso.")
    else:
        print("\nValor inválido.")
    pass

def sacar_dinheiro():
    global saldo
    valor = float(input("\nDigite o valor a ser sacado R$ "))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        salvar_no_csv("Saque", valor)
        print(f"\nSaque de R$ {valor} realizado com sucesso.")
    else:
        print("\nSaldo insuficiente ou valor inválido.")
    pass

def ver_extrato():
    print("\n===== EXTRATO =====")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    pass

def movimentacao():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.plot(x, y, color="blue", linestyle="--", marker="o")

    plt.title("Sample Line Chart")
    plt.xlabel("X Axis Label")
    plt.ylabel("Y Axis Label")

    plt.show()
    pass

def main():
    while True:
        exibir_banco()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            consultar_saldo()
        elif opcao == "2":
            depositar_dinheiro()
        elif opcao == "3":
            sacar_dinheiro()
        elif opcao == "4":
            ver_extrato()
        elif opcao == "5":
            movimentacao()
        elif opcao == "6":
            print("\nSaindo do sistema. Obrigado por utilizar o Caixa Eletrônico.")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")

main()