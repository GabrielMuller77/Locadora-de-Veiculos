from Database.crud_usuario import *
from Database.crud_veiculo import *
from Database.validar_database import *
from Database.crud_aluguel import *

def main():
    while True:
        login = ler_int("MENU DE LOGIN\n1 - Usuários\n2 - Veículos\n3 - Alugar e Devolver\n4 - SAIR\nOpção: ")
        match login:
            case 1:
                while True:
                    menu_cliente = ler_int("MENU CLIENTE\n1 - CADASTRAR USUÁRIO\n2 - CONSULTAR USUÁRIOS\n3 - LISTAR USUÁRIOS\n4 - EXCLUIR USUÁRIO\n5 - ATUALIZAR USUÁRIOS\n6 - SAIR\nOpção: ")
                    match menu_cliente:
                        case 1:
                            criar_usuario()
                        case 2:
                            consultar_usuario()
                        case 3:
                            listar_usuario()
                        case 4:
                            excluir_usuario()
                        case 5:
                            atualizar_cadastro()
                        case 6:
                            print("Saindo...")
                            break
                        case _:
                            print("Opção inválida, tente novamente.")
            case 2:
                while True:
                    menu_veiculos = ler_int("MENU VEÍCULOS\n1 - CADASTRAR VEÍCULO\n2 - BUSCAR VEÍCULOS\n3 - LISTAR VEÍCULOS\n4 - EXCLUIR VEÍCULO\n5 - ATUALIZAR VEÍCULO\n6 - SAIR\nOpção: ")
                    match menu_veiculos:
                        case 1:
                            cadastrar_veiculo()
                        case 2:
                            buscar_veiculo()
                        case 3:
                            listar_veiculo()
                        case 4:
                            excluir_veiculo()
                        case 5:
                            atualizar_veiculo()
                        case 6:
                            print("Saindo...")
                            break 
                        case _:
                            print("Opção inválida, tente novamente.")
            case 3:
                while True:
                    opcao = ler_int("MENU PRINCIPAL\n1 - ALUGAR\n2 - DEVOLVER\n3 - BUSCAR ALUGUEL\n4 - LISTAR ALUGUÉIS\n5 - SAIR\nOPÇÃO: ")
                    match opcao:
                        case 1:
                            cadastrar_aluguel()
                        case 2:
                            devolver()
                        case 3:
                            buscar_aluguel()
                        case 4:
                            lista_filtrada_alugueis()
                        case 5:
                            print("Saindo...")
                            break
                        case _:
                            print("Opção inválida, tente novamente.")
            case 4:
                break
            case _:
                print("Opção inválida, tente novamente.")        





if __name__ == '__main__':
    main()