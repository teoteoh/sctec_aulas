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
    "1001": {"nome": "Usuário Exemplo", "senha": "1234"},
    "1002": {"nome": "Usuário 1002", "senha": "1234"},
    "1003": {"nome": "Usuário 1003", "senha": "1234"},
    "1004": {"nome": "Usuário 1004", "senha": "1234"},
}