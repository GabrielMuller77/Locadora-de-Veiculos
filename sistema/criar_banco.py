from Database.database import Base, db
from Database.modelos import Usuario, Veiculo, Aluguel

print("Tabelas antes:", Base.metadata.tables.keys())

Base.metadata.create_all(db)

print("Tabelas depois:", Base.metadata.tables.keys())
print("Banco e tabelas criados!")