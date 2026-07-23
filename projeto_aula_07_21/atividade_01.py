import csv  
#importa funcionalidades para lidar com csv

import os   
#importa funcionalidades de OS

from datetime import date, datetime, timedelta  
#importa da biblioteca datetime funcoes relacionadas a data e hora

ARQUIVO_CSV = "cadastro_matricula.csv"
CAMPOS = ["matricula", "nome", "data", "entrada", "saida_almoco", "retorno_almoco", "saida"]
JORNADA_PADRAO = timedelta(hours=8)

CREDENCIAIS = {
    "robisvaldo_fagundes": {"nome": "Robisvaldo Lima Fagundes", "senha": "1234"},
    "antoninho_pereira": {"nome": "Antoninho Pereira", "senha": "1234"},
    "dagoberta_sinclair": {"nome": "Dagoberta Sinclair da Silva", "senha": "1234"},
    "claudineia_nocciolini": {"nome": "claudineia_nocciolini", "senha": "1234"},
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