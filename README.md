📦 API de Produtos - FastAPI + SQLAlchemy + SQLite

API REST para gerenciamento de produtos, construída com FastAPI, SQLAlchemy e SQLite, seguindo boas práticas de separação entre models, schemas e database.

🚀 Tecnologias utilizadas
FastAPI
SQLAlchemy
Pydantic
SQLite (banco local)

📁 Estrutura do projeto
.
├── main.py
├── database.py
├── models.py
├── schemas.py
└── produtos.db

⚙️ Funcionalidades

A API permite:

Criar produtos
Listar todos os produtos
Buscar produto por ID
Atualizar produto
Deletar produto

🗄️ Banco de dados

O projeto utiliza SQLite local, criado automaticamente como:

produtos.db

A tabela é criada automaticamente ao iniciar a aplicação:

models.Base.metadata.create_all(bind=engine)


▶️ Como executar o projeto
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>

Instale as dependências
pip install fastapi sqlalchemy uvicorn pydantic

Execute o servidor
uvicorn main:app --reload

🧠 Observações técnicas
O ORM utilizado é o SQLAlchemy
Os schemas utilizam Pydantic com from_attributes = True
A conexão com banco é feita via SessionLocal
O banco é SQLite com check_same_thread=False


📄 Licença
Projeto para fins de estudo e aprendizado.
