from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./produtos.db"
#CRIA A CONEXÃO COM O BANCO DE DADOS
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

#CONTRUTOR DE SESSÕES
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
