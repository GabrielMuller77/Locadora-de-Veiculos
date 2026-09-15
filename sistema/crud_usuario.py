from Database.database import session
from Database.modelos import Usuario, Aluguel
from Database.validar_database import validar_usuario, ler_int, validar_email, validar_nome
from Database.utilidades import perguntar_novamente, validar_sn
from werkzeug.security import generate_password_hash


def criar_usuario():
    while True:
        nome = validar_nome()
        email = validar_email()
        usuario_existente = session.query(Usuario).filter_by(email=email).first()
        if usuario_existente:
            print("Email já cadastrado, tente novamente.")
            continue
        senha = input("Senha: ")
        usuario = Usuario(
            nome=nome,
            email=email,
            senha=generate_password_hash(senha)
        )
        session.add(usuario)
        session.commit()
        break


def consultar_usuario():
    while True:
        print("MENU DE CONSULTA\n1 - BUSCAR TODOS\n2 - BUSCAR PELO ID\n3 - BUSCAR PELO EMAIL\n4 - SAIR")
        escolha = ler_int("Opção: ")
        match escolha:
            case 1:
                listar_usuario()
            case 2:
                while True:
                    id_usuario = ler_int("ID: ")
                    usuario = session.query(Usuario).filter_by(id=id_usuario).first()
                    if validar_usuario(usuario):
                        listar_um(usuario)
                        break
                    else:
                        if perguntar_novamente():
                            continue 
                        else:
                            print("Encerrando a consulta por ID.")
                            break           
            case 3:
                while True:
                    email_usuario = validar_email()
                    usuario = session.query(Usuario).filter_by(email=email_usuario).first()
                    if validar_usuario(usuario):
                        listar_um(usuario)
                        break
                    else:
                        if perguntar_novamente():
                            continue
                        else:
                            print("Encerrando consulta por Email.")    
                            break            
            case 4:
                print("Saindo...")
                break
            case _:
                print("Opção inválida, tente novamente")


def listar_um(usuario):
    status = "Ativo" if usuario.ativo else "Inativo"
    print("\n" + "=" * 40)
    print(f"ID:       {usuario.id}")
    print(f"NOME:     {usuario.nome}")
    print(f"EMAIL:    {usuario.email}")
    print(f"STATUS:   {status}")
    print("=" * 40)


def listar_usuario():
    usuarios = session.query(Usuario).all()
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
        return
    print("\n" + "#" * 40)
    print("          USUÁRIOS CADASTRADOS")
    print("#" * 40)
    for usuario in usuarios:
        listar_um(usuario)



def excluir_usuario():
    while True:
        listar_usuario()
        id_exclusao = ler_int('Informe o ID do usuário que deseja excluir, 0 para cancelar: ')
        if id_exclusao == 0:
            print('Operação cancelada')
            return
        usuario = session.query(Usuario).filter_by(id=id_exclusao).first()
        aluguel = session.query(Aluguel).filter_by(id_usuario=id_exclusao).first()
        if validar_usuario(usuario):
            if not aluguel:
                verificador = validar_sn(f'Tem certeza que deseja excluir o usuario {id_exclusao}, [S/N]: ')
                if verificador:
                    session.delete(usuario)
                    session.commit()
                    print('Usuário excluído, encerrando sistema de exclusão.')
                    return
                else:
                    print("Exclusão cancelada, retornando.")
                    return
            else:
                print("Usuário vinculado a aluguel de veículo, não foi possível excluir")
                break
        else:
            print("Usuário não encontrado, tente novamente")


def atualizar_cadastro():
    while True:
        listar_usuario()
        print('MENU DE ATUALIZAÇÕES DE USUÁRIO\n1 - ATUALIZAR TUDO\n 2 - ATUALIZAR NOME\n 3 - ATUALIZAR EMAIL\n4 - ATUALIZAR STATUS\n5 - SAIR')
        opcao = ler_int('Opção: ')
        match opcao:
            case 1:
                while True:
                    id_atualizar = ler_int("Qual o ID do usuário que deseja atualizar: ")
                    novo_nome = validar_nome()
                    novo_email = validar_email()
                    email_duplicado = session.query(Usuario).filter_by(email=novo_email).first()
                    usuario = session.query(Usuario).filter_by(id=id_atualizar).first()
                    if validar_usuario(usuario):
                        if email_duplicado and  email_duplicado.id != usuario.id:
                            print("Email já cadastrado, tente novamente.")
                            continue
                        usuario.nome = novo_nome
                        usuario.email = novo_email
                        status = validar_sn("Deseja alterar o status? [S/N]: ")
                        if status: 
                            usuario.ativo = not usuario.ativo
                            print(f'Nome, Email e Status do usuário {usuario.id} alterados com sucesso.')
                        else:
                            print(f'Nome e Email do usuário {usuario.id} alterados com sucesso.')
                        session.commit()
                        break
            case 2:
                novo_nome = validar_nome()
                id_atualizar = ler_int("Qual o ID do usuário que deseja atualizar: ")
                usuario = session.query(Usuario).filter_by(id=id_atualizar).first()
                if validar_usuario(usuario):
                    usuario.nome = novo_nome
                    session.commit()
                    print(f'Nome do usuário {usuario.id} alterado com sucesso.')
            case 3:
                while True:
                    id_atualizar = ler_int("Qual o ID do usuário que deseja atualizar: ")
                    novo_email = validar_email()
                    email_duplicado = session.query(Usuario).filter_by(email=novo_email).first()
                    usuario = session.query(Usuario).filter_by(id=id_atualizar).first()
                    if validar_usuario(usuario):
                        if email_duplicado and email_duplicado.id != usuario.id:
                            print("Email já cadastrado, tente novamente.")
                            continue
                        usuario.email = novo_email
                        session.commit()
                        print(f'Email do usuário {usuario.id} alterado com sucesso.')
            case 4:
                id_atualizar = ler_int("Qual o ID do usuário que deseja atualizar: ")
                usuario = session.query(Usuario).filter_by(id=id_atualizar).first()
                if validar_usuario(usuario):
                    usuario.ativo = not usuario.ativo
                    session.commit()
                    print(f'Status do usuário {usuario.id} alterado com sucesso.')
            case 5:
                print("Encerrando programa de atualização.")
                break
            case _:
                print("Opção inválida, tente novamente.")




