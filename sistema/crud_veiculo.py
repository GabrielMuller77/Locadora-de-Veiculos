from Database.database import session
from Database.modelos import Veiculo, Aluguel
from Database.validar_database import ler_int, validar_veiculo, validar_placa, validar_usuario, validar_tipo, ler_valor, validar_modelo
from Database.utilidades import perguntar_novamente, validar_sn

def cadastrar_veiculo():
    while True:
        modelo = validar_modelo()
        placa = validar_placa()
        if placa == "CANCELADO":
            return
        placa_duplicada = session.query(Veiculo).filter_by(placa=placa).first()
        if placa_duplicada:
            print("Placa duplicada, tente novamente.")
            continue
        valor_diario = ler_valor("Valor diário: ") 
        veiculo_tipo = validar_tipo()
        veiculo = Veiculo(
            modelo=modelo,
            placa=placa,
            tipo=veiculo_tipo,
            valor_diario=valor_diario
        )
        session.add(veiculo)
        session.commit()
        print(veiculo.status)


def buscar_veiculo():
     while True:
        print("MENU DE BUSCA\n1 - BUSCAR TODOS\n2 - BUSCAR POR ID\n3 - BUSCAR POR MODELO\n4 - BUSCAR POR PLACA\n5 - BUSCAR POR STATUS\n6 - SAIR")
        escolha = ler_int("Sua opção: ")
        match escolha:
            case 1:
                listar_veiculo()
            case 2:
                while True:
                    id_veiculo = ler_int("ID: ")
                    veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                    if validar_veiculo(veiculo):
                        lista_um_veiculos(veiculo)
                        break
                    else:
                        if perguntar_novamente():
                            continue
                        else:
                            print("Encerrando a busca por ID.")
                            break
            case 3:
                while True:
                    modelo_veiculo = input("Modelo do veículo: ")
                    veiculo = session.query(Veiculo).filter_by(modelo=modelo_veiculo).first()
                    if validar_veiculo(veiculo):
                        lista_um_veiculos(veiculo)
                        break
                    else:
                        if perguntar_novamente():
                            continue
                        else:
                            print("Encerrando a busca por Modelo.")
                            break
            case 4:
                while True:
                    placa_veiculo = validar_placa()
                    if placa_veiculo == "CANCELADO":
                        return
                    veiculo = session.query(Veiculo).filter_by(placa=placa_veiculo).first()
                    if validar_veiculo(veiculo):
                        lista_um_veiculos(veiculo)
                        break
                    else:
                        if perguntar_novamente():
                            continue
                        else:
                            print("Encerrando a buscar por Placa.")
                            break
            case 5:
                while True:
                    status_veiculo = ler_int("1 - Alugado\n2 - Disponível")
                    if status_veiculo ==  1:
                        veiculo = session.query(Veiculo).filter_by(status=False).all()
                        for v in veiculo:
                            lista_um_veiculos(v)
                        break
                    elif status_veiculo == 2:
                        veiculo = session.query(Veiculo).filter_by(status=True).all()
                        for v in veiculo:
                            lista_um_veiculos(v)
                        break
                    else:
                        if perguntar_novamente():
                            continue
                        else:
                            print("Encerrando busca por Status.")
                            break
            case 6:
                print("Encerrando menu de busca...")
                break
            case _:
                print("Opção inválida, tente novamente.")


def lista_um_veiculos(veiculo):
    status = "Disponível" if veiculo.status else "Alugado"
    print("\n" + "=" * 50)
    print(f"ID:              {veiculo.id}")
    print(f"MODELO:          {veiculo.modelo}")
    print(f"TIPO:            {veiculo.tipo}")
    print(f"PLACA:           {veiculo.placa}")
    print(f"VALOR DIÁRIO:    R$ {veiculo.valor_diario:.2f}")
    print(f"STATUS:          {status}")
    print("=" * 50)


def listar_veiculo():
    veiculos = session.query(Veiculo).all()
    if not veiculos:
        print("\nNenhum veículo cadastrado.")
        return
    print("\n" + "#" * 50)
    print("              VEÍCULOS CADASTRADOS")
    print("#" * 50)
    for veiculo in veiculos:
        lista_um_veiculos(veiculo)

def excluir_veiculo():
    while True:
        listar_veiculo()
        id_exclusao = ler_int("ID do veículo que deseja excluir: ")
        if id_exclusao == 0:
            print('Operação cancelada')
            return
        veiculo = session.query(Veiculo).filter_by(id=id_exclusao).first()
        aluguel = session.query(Aluguel).filter_by(id_veiculo=id_exclusao).first()
        if validar_veiculo(veiculo):
            if not aluguel:
                verificador = validar_sn(f'Tem certeza que deseja excluir o veículo {id_exclusao}, [S/N]: ')
                if verificador:
                    session.delete(veiculo)
                    session.commit()
                    print('Veículo excluído, encerrando sistema de exclusão.')
                    return
                else:
                    print('Exclusão cancelada, encerrando sistema de exclusão.')
            else:
                print("Veículo possui histórico de aluguel e não pode ser excluído.")        
        else:
            print('Veículo não encontrado, tente novamente.')


def atualizar_veiculo():
    while True:
        print("MENU ATUALIZAR\n 1 - ATUALIZAR TUDO\n2 - ATUALIZAR MODELO\n3 - ATUALIZAR PLACA\n4 - ATUALIZAR VALOR DIÁRIO\n5 - SAIR")
        opcao = ler_int("Opção: ")
        match opcao:
            case 1:
                while True:
                    id_veiculo = ler_int("ID do veículo: ")
                    novo_modelo = validar_modelo()
                    nova_placa = validar_placa()
                    if nova_placa == "CANCELADO":
                        break
                    placa_duplicada = session.query(Veiculo).filter_by(placa=nova_placa).first()
                    veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                    if validar_veiculo(veiculo):
                        if placa_duplicada and placa_duplicada.id != veiculo.id:
                            print("Placa já cadastrada, tente novamente.")
                            continue
                        novo_valor = ler_valor("Novo valor diário: ")
                        veiculo.modelo = novo_modelo
                        veiculo.placa = nova_placa
                        veiculo.valor_diario = novo_valor
                        session.commit()
                        print("Veículo atualizado com sucesso.")
                    else:
                        print("Veículo não encontrado.")
            case 2:
                id_veiculo = ler_int("ID do veículo: ")
                novo_modelo = validar_modelo()
                veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                if validar_veiculo(veiculo):
                    veiculo.modelo = novo_modelo
                    session.commit()
            case 3:
                id_veiculo = ler_int("ID do veículo: ")
                nova_placa = validar_placa()
                if nova_placa == "CANCELADO":
                    break
                placa_duplicada = session.query(Veiculo).filter_by(placa=nova_placa).first()
                veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                if validar_veiculo(veiculo):
                    if placa_duplicada and placa_duplicada.id != veiculo.id:
                        veiculo.placa = nova_placa
                        session.commit()
            case 4:
                id_veiculo = ler_int("ID do veículo: ")
                novo_valor = ler_valor("Novo valor: ")
                veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                if validar_veiculo(veiculo):
                    veiculo.valor_diario = novo_valor
                    session.commit()

            case 5:
                print("Encerrando o sistema de atualização.")
                break
            case _:
                print("Opção inválida, tente novamente.")
