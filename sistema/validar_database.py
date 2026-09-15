from Database.utilidades import perguntar_novamente
from datetime import datetime
from decimal import Decimal, InvalidOperation
import re

def validar_usuario(usuario):
    if usuario is None:
        print('Usuário não encontrado.')
    return usuario

def validar_veiculo(veiculo):
    if veiculo is None:
        print("Veículo não encontrado.")
    return veiculo

def validar_aluguel(aluguel):
    if aluguel is None:
        print("Aluguel não encontrado.")
    return aluguel


def ler_int(msg):
    while True:
        valor = input(msg) 
        try:
            valor_int = int(valor)
            if valor_int >= 0:
                return valor_int
            else:
                print("Digite um número maior ou igual a 0.")
                continue
        except ValueError:
            print('Digite um número válido.')


def validar_placa():
    validacao = re.compile(r'[A-Z]{3}[0-9]{4}|[A-Z]{3}[0-9][A-Z][0-9]{2}')
    while True:
        placa = input("Placa: ").strip().upper()
        if validacao.fullmatch(placa):
            print("Placa cadastrada: ")
            return placa
        else:
            print("Modelo de placa inválido, tente novamente.")


def ler_data(mensagem):
    while True:
        try:
            data = input(mensagem)
            data = datetime.strptime(data, "%d/%m/%Y").date()
            return data
        except ValueError:
            print("Digite uma data válida. Exemplo: 28/08/2026")


def validar_tipo():
    while True:
        mensagem = input("Tipo do veículo: ").strip().capitalize()
        if mensagem in ("Carro", "Moto", "Caminhão"):
            return mensagem
        print("Tipo de veículo inválido, tente novamente com (Carro, Moto ou Caminhão).")


def validar_email():
    validacao = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+')
    while True:
        email = input("Email: ")
        if validacao.fullmatch(email):
            return email
        else:
            print("Email inválido, tente novamente.")

def ler_valor():
    while True:
        try:
            valor = Decimal(input("Valor: ").replace(",", ".").strip())
            if valor <= 0:
                print("Valor inválido, por favor digite um número positivo.")
                continue
            return valor
        except InvalidOperation:
            print("Valor inválido, por favor digite um número válido.")

def validar_nome():
    while True:
        nome = input("Nome: ").strip()
        if not nome.strip():
            print("Nome vazio inválido, digite um nome válido.")
            continue
        return nome


def validar_modelo():
    while True:
        modelo = input("Modelo: ").strip()
        if not modelo.strip():
            print("Modelo vazio inválido, digite um modelo válido.")
            continue
        return modelo

