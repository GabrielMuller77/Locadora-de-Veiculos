def perguntar_novamente():
    while True:
        escolha = input('Tentar novamente, [S/N]? ').upper().strip()
        if escolha and escolha[0] == "S":
            return True
        elif escolha and escolha[0] == "N":
            return False
        else:
            continue

def validar_sn(msg):
    while True:
        escolha = input(msg).upper().strip()
        if escolha and escolha[0] == "S":
            return True
        elif escolha and escolha[0] == "N":
            return False
        else:
            print("Opção inválida, digite S ou N.")
                