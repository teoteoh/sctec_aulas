# problema 1: toda vez que o sistema for pesquisar matricula, tem que verificar o próximo segmento.
# problema 2: não adicionar horário. apenas matricula e senha.
# problema 3: só bate horário se horário anterior for batido.
# problema 4: horário só pode ser batido em horários específicos.

user = int(input("Usuário: "))
senha = int(input("Senha: "))
entrada = 0
almoco = 0
almoco_volta = 0
saida = 0
ponto = 0

if user == 123 and senha == 123:
    while ponto <= 5:
        match ponto:
            case 1:
                entrada = float(input("Horário de entrada: "))
                if entrada < 7 or entrada > 12:
                    print("Horário inválido. Favor entrar em contato com supervisor.")
            
            case 2:
                almoco = float(input("Horário que saiu para o almoço: "))
                if almoco < 12 or almoco > 14:
                    print("Horário de almoço inválido. Favor entrar em contato com supervisor.")
            
            case 3:
                almoco_volta = float(input("Horário que voltou do almoço: "))
                if almoco_volta > 15:
                    print("Horário de almoço inválido. Favor entrar em contato com supervisor.")
            
            case 4:
                saida = float(input("Horário do fim do expediente: "))
                if saida < 17:
                    print("Horário de saída inválida. Favor entrar em contato com supervisor.")
            
            case 5:
                print(f"Horário de entrada: {entrada:.2f}\n"
                      f"Horário de almoço: {almoco:.2f}\n"
                      f"Horário da volta do almoço: {almoco_volta:.2f}\n"
                      f"Horário da saída: {saida:.2f}")
            
                pass
        
        ponto += 1
else: 
    print("Usuário ou senha inválidos.")