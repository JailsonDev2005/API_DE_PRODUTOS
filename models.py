from sqlalchemy import Column, Integer, String, Float
from database import Base


#CRIA UMA TABELA NO BANCO DE DADOS
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    preco = Column(Float)
    descricao = Column(String)
