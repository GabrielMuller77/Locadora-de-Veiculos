from Database.modelos import Usuario, Veiculo, Aluguel
from Database.database import session 
from Database.crud_veiculo import lista_um_veiculos
from Database.utilidades import validar_sn
from Database.validar_database import ler_data, ler_int, validar_usuario, validar_veiculo, validar_aluguel
from datetime import date
from Database.classes import Carro, Moto, Caminhao

def cadastrar_aluguel():
    while True:
        print("VEÍCULOS DISPONÍVEIS")
        veiculos = session.query(Veiculo).filter_by(status=True).all()
        if veiculos:
            for veiculo in veiculos:
                lista_um_veiculos(veiculo)
        else:
            print("Não há veículos disponíveis no momento, tente novamente mais tarde.")
            return
        id_locatario = ler_int("Seu ID: ")
        usuario = session.query(Usuario).filter_by(id=id_locatario, ativo=True).first()
        id_veiculo = ler_int("ID do veículo que deseja alugar: ")
        veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
        if validar_usuario(usuario) and validar_veiculo(veiculo):
            if not veiculo.status:
                print("Esse veículo já está alugado.")
                continue
            data_inicio = date.today()
            data_fim = ler_data("Data final: ")
            if data_fim <= data_inicio:
                print("A data de devolução precisa ser posterior a data de início.")
                continue
            dias = (data_fim - data_inicio).days
            valor_diario = veiculo.valor_diario
            tipo = veiculo.tipo
            if tipo == "Carro":
                veiculo_pagamento = Carro(valor_diario)
            elif tipo == "Moto":
                veiculo_pagamento = Moto(valor_diario)
            elif tipo == "Caminhão":
                veiculo_pagamento = Caminhao(valor_diario)
            valor_total = veiculo_pagamento.calcular_valor_total(dias)
            aluguel = Aluguel(
                id_usuario = id_locatario,
                id_veiculo = id_veiculo,
                data_inicio= data_inicio,
                data_fim = data_fim,
                valor_diario = valor_diario,
                valor_total = valor_total,
                multa = 0
                )
            
            print(f"Dias alugados: {dias}")
            print(f"Valor total: R$ {valor_total}")
            controle = validar_sn("Deseja alugar o veículo?[S/N]: ")
            if controle:
                session.add(aluguel)
                veiculo.status = False
                session.commit()
                print("Veículo alugado com sucesso.")
                break
            else:
                print("Sistema de aluguel encerrado.")
                return   


def lista_um_aluguel(aluguel):
    print("\n" + "=" * 50)
    print(f"ID:              {aluguel.id}")
    print(f"ID USUÁRIO:      {aluguel.id_usuario}")
    print(f"ID VEÍCULO:      {aluguel.id_veiculo}")
    print(f"DATA INÍCIO:     {aluguel.data_inicio.strftime('%d/%m/%Y')}")
    print(f"DATA FIM:        {aluguel.data_fim.strftime('%d/%m/%Y')}")
    if aluguel.data_devolucao is None:
        print("STATUS:          ALUGADO")
        print("DATA DEVOLUÇÃO:  Ainda não devolvido")
    else:
        print("STATUS:          DEVOLVIDO")
        print(f"DATA DEVOLUÇÃO:  {aluguel.data_devolucao.strftime('%d/%m/%Y')}")
    print(f"VALOR DIÁRIO:    R$ {aluguel.valor_diario:.2f}")
    print(f"VALOR TOTAL:     R$ {aluguel.valor_total:.2f}")
    if aluguel.multa > 0:
        print(f"MULTA:       {aluguel.multa}")
    print("=" * 50)


def listar_alugueis():
    alugueis = session.query(Aluguel).all()
    if not alugueis:
        print("Nenhum aluguel cadastrado.")
        return
    print("\n" + "#" * 50)
    print("              ALUGUÉIS CADASTRADOS")
    print("#" * 50)
    for aluguel in alugueis:
        lista_um_aluguel(aluguel)

def lista_filtrada_alugueis():
    while True:
        opcao = ler_int("OPÇÕES DE LISTAGEM\n1 - LISTAR TODOS\n2 - LISTAR ATIVOS\n3 - LISTAR DEVOLVIDOS\n4 - SAIR")
        match opcao:
            case 1:
                listar_alugueis()
            case 2:
                alugueis = session.query(Aluguel).filter_by(data_devolucao=None).all()
                for aluguel in alugueis:
                    lista_um_aluguel(aluguel)
            case 3:
                alugueis = session.query(Aluguel).filter(
                    Aluguel.data_devolucao.is_not(None)
                ).all()
                for aluguel in alugueis:
                    lista_um_aluguel(aluguel)
            case 4:
                print("Encerrando...")
                break
            case _:
                print("Opção inválida.")
                


def devolver():
    while True:
        veiculos = session.query(Veiculo).filter_by(status=False).all()
        if not veiculos:
            print("Nenhum veículo alugado no momento.")
            return
        print("VEÍCULOS ALUGADOS")
        for veiculo in veiculos:
            lista_um_veiculos(veiculo)
        id_locatario = ler_int("ID do locatário: ")
        id_veiculo = ler_int("ID do veículo: ")
        aluguel = session.query(Aluguel).filter_by(id_usuario=id_locatario, id_veiculo=id_veiculo, data_devolucao=None).first()
        veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
        if validar_aluguel(aluguel) and validar_veiculo(veiculo):
            veiculo.status = True
            aluguel.data_devolucao = date.today()
            dias_atraso = (aluguel.data_devolucao - aluguel.data_fim).days
            if dias_atraso <= 0:
                dias_atraso = 0
            aluguel.multa = aluguel.valor_diario * dias_atraso
            session.commit()
            print("Veículo devolvido com sucesso.")
            print(f"Data prevista: {aluguel.data_fim}")
            print(f"Data devolução: {aluguel.data_devolucao}")
            print(f"Dias de atraso: {dias_atraso}")
            print(f"Multa: {aluguel.multa}")
            break

def buscar_aluguel():
    while True:
        opcao = ler_int("MENU DE BUSCA DE ALUGUEL\n1 - BUSCAR POR ID\n2 - BUSCAR POR ID DE USUÁRIO\n3 - BUSCAR POR ID DE VEÍCULO\n4 - BUSCAR POR DATA DE INÍCIO\n5 - BUSCAR POR DATA FINAL\n6 - BUSCAR POR  DATA DE DEVOLUÇÃO\n7 - SAIR\nOPÇÃO: ")
        match opcao:
            case 1:
                id_aluguel = ler_int("ID do aluguel: ")
                aluguel = session.query(Aluguel).filter_by(id=id_aluguel).first()
                if validar_aluguel(aluguel):
                    lista_um_aluguel(aluguel)
            case 2:
                id_usuario = ler_int("ID do usuário: ")
                alugueis = session.query(Aluguel).filter_by(id_usuario=id_usuario).all()
                if alugueis:
                    for aluguel in alugueis:
                        lista_um_aluguel(aluguel)
            case 3:
                id_veiculo = ler_int("ID do veículo: ")
                alugueis = session.query(Aluguel).filter_by(id_veiculo=id_veiculo).all()
                if alugueis:
                    for aluguel in alugueis:
                        lista_um_aluguel(aluguel)
            case 4:
                data_inicio = ler_data("Data de início: ")
                alugueis = session.query(Aluguel).filter_by(data_inicio=data_inicio).all()
                if alugueis:
                    for aluguel in alugueis:
                        lista_um_aluguel(aluguel)
                else:
                    print("Nenhum aluguel encontrado.")
            case 5:
                data_fim = ler_data("Data final: ")
                alugueis = session.query(Aluguel).filter_by(data_fim=data_fim).all()
                if alugueis:
                    for aluguel in alugueis:
                        lista_um_aluguel(aluguel)
                else:
                    print("Nenhum aluguel encontrado.")
            case 6:
                data_devolucao = ler_data("Data final: ")
                alugueis = session.query(Aluguel).filter_by(data_devolucao=data_devolucao).all()
                if alugueis:
                    for aluguel in alugueis:
                        lista_um_aluguel(aluguel)
                else:
                    print("Nenhum aluguel encontrado.")
            case 7:
                print("Encerrando...")
                break 
            case _:
                print("Opção inválida, tente novamente.")