import csv
import os
from datetime import date, datetime, timedelta

ARQUIVO_CSV = "registros_pontos.csv"
CAMPOS = ["matricula", "nome", "data", "entrada", "saida_almoco", "retorno_almoco", "saida"]
JORNADA_PADRAO = timedelta(hours=8)

CREDENCIAIS = {
    "1001": {"nome": "Usuário Exemplo", "senha": "1234"},
    "1002": {"nome": "Usuário 1002", "senha": "1234"},
    "1003": {"nome": "Usuário 1003", "senha": "1234"},
    "1004": {"nome": "Usuário 1004", "senha": "1234"},
}
usuario = ["", "", "", "", "", ""]


def calcular_horas_trabalhadas(usuario):
    entrada, saida_almoco, retorno_almoco, saida = usuario[2], usuario[3], usuario[4], usuario[5]
    if not (entrada and saida_almoco and retorno_almoco and saida):
        return None

    formato = "%H:%M"
    periodo_manha = datetime.strptime(saida_almoco, formato) - datetime.strptime(entrada, formato)
    periodo_tarde = datetime.strptime(saida, formato) - datetime.strptime(retorno_almoco, formato)
    return periodo_manha + periodo_tarde


def formatar_duracao(duracao):
    total_minutos = int(duracao.total_seconds()) // 60
    horas, minutos = divmod(total_minutos, 60)
    return f"{horas:02d}:{minutos:02d}"


def carregar_registro_do_dia(matricula):
    hoje = date.today().isoformat()
    if not os.path.exists(ARQUIVO_CSV):
        return

    with open(ARQUIVO_CSV, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha["matricula"] == matricula and linha["data"] == hoje:
                usuario[2] = linha["entrada"]
                usuario[3] = linha["saida_almoco"]
                usuario[4] = linha["retorno_almoco"]
                usuario[5] = linha["saida"]
                return


def salvar_registro_do_dia(matricula):
    hoje = date.today().isoformat()
    linha_atual = {
        "matricula": matricula,
        "nome": usuario[0],
        "data": hoje,
        "entrada": usuario[2],
        "saida_almoco": usuario[3],
        "retorno_almoco": usuario[4],
        "saida": usuario[5],
    }

    linhas = []
    encontrado = False

    if os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                if linha["matricula"] == matricula and linha["data"] == hoje:
                    linha = linha_atual
                    encontrado = True
                linhas.append(linha)

    if not encontrado:
        linhas.append(linha_atual)

    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(linhas)


while True:
    print("\n=== Sistema de Ponto ===")
    print("1 - Login")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        matricula = input("Matrícula: ")
        senha = input("Senha: ")

        if matricula in CREDENCIAIS and senha == CREDENCIAIS[matricula]["senha"]:
            usuario[0] = CREDENCIAIS[matricula]["nome"]
            usuario[1] = senha
            usuario[2] = usuario[3] = usuario[4] = usuario[5] = ""
            carregar_registro_do_dia(matricula)
            while True:
                print("\n--- Menu de", usuario[0], "---")
                print("1 - Registrar ponto")
                print("2 - Ver registros")
                print("0 - Voltar")

                opcao2 = input("Escolha uma opção: ")

                if opcao2 == "1":
                    hora = input("Digite o horário atual (ex: 08:00): ")

                    if usuario[2] == "":
                        usuario[2] = hora
                        print("Entrada registrada às", hora)
                    elif usuario[3] == "":
                        usuario[3] = hora
                        print("Saída para o almoço registrada às", hora)
                    elif usuario[4] == "":
                        usuario[4] = hora
                        print("Retorno do almoço registrado às", hora)
                    elif usuario[5] == "":
                        usuario[5] = hora
                        print("Saída registrada às", hora)
                    else:
                        print("Todos os pontos do dia já foram registrados.")

                    salvar_registro_do_dia(matricula)

                elif opcao2 == "2":
                    print("\nExtrato de ponto de", usuario[0])
                    print("Entrada:        ", usuario[2] or "--:--")
                    print("Saída almoço:   ", usuario[3] or "--:--")
                    print("Retorno almoço: ", usuario[4] or "--:--")
                    print("Saída:          ", usuario[5] or "--:--")

                    horas_trabalhadas = calcular_horas_trabalhadas(usuario)
                    if horas_trabalhadas is None:
                        print("Jornada incompleta: registre todos os pontos do dia para ver o total de horas.")
                    else:
                        print("Total trabalhado:", formatar_duracao(horas_trabalhadas))
                        if horas_trabalhadas < JORNADA_PADRAO:
                            print("Faltam", formatar_duracao(JORNADA_PADRAO - horas_trabalhadas), "para completar a jornada de 8h.")
                        elif horas_trabalhadas > JORNADA_PADRAO:
                            print("Hora extra:", formatar_duracao(horas_trabalhadas - JORNADA_PADRAO), "além da jornada de 8h.")
                        else:
                            print("Jornada de 8h cumprida exatamente.")

                elif opcao2 == "0":
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Matrícula ou senha inválida.")

    elif opcao == "0":
        print("Até mais!")
        break

    else:
        print("Opção inválida.")
