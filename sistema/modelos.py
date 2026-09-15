from Database.database import Base
from sqlalchemy import Integer, String, Boolean, ForeignKey, Column, Date, Numeric
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, default=True)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    modelo = Column("modelo", String, nullable=False)
    placa = Column("placa", String, unique=True, nullable=False)
    tipo = Column("tipo", String, nullable=False)
    valor_diario = Column("valor_diario", Numeric(10, 2), nullable=False)
    status = Column("status", Boolean, default=True)

    def __init__(self, modelo, placa, tipo, valor_diario, status=True):
        self.modelo = modelo
        self.placa = placa
        self.tipo = tipo
        self.valor_diario = valor_diario
        self.status = status


class Aluguel(Base):
    __tablename__ = "alugueis"


    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_usuario = Column("id_usuario", Integer, ForeignKey("usuarios.id"), nullable=False)
    id_veiculo = Column("id_veiculo", Integer, ForeignKey("veiculos.id"), nullable=False)
    data_inicio = Column("data_inicio", Date, nullable=False)
    data_fim = Column("data_fim", Date, nullable=False)
    data_devolucao = Column("data_devolucao", Date, nullable=True)
    valor_diario = Column("valor_diario", Numeric(10, 2), nullable=False)
    valor_total = Column("valor_total", Numeric(10, 2), nullable=False)
    multa = Column("multa", Numeric(10, 2), nullable=False, default=0)


    def __init__(self, id_usuario, id_veiculo, data_inicio, data_fim, valor_diario, valor_total, multa, data_devolucao = None):
        self.id_usuario = id_usuario
        self.id_veiculo = id_veiculo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.data_devolucao = data_devolucao
        self.valor_diario = valor_diario
        self.valor_total = valor_total
        self.multa = multa