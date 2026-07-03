from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#ROTA PARA MOSTRA OS PRODUTOS
@app.get("/produtos", response_model=list[schemas.Produto])
def lista_produtos(db: Session = Depends(get_db)):
    return db.query(models.Produto).all()


#ROTA PARA CRIAS PRODUTOS
@app.post('/produtos', response_model=schemas.Produto)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):

    novo_produto = models.Produto(
        titulo=produto.titulo,
        preco=produto.preco,
        descricao=produto.descricao
    )


    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto


#ROTA BUSCA PRODUTO POR ID
@app.get('/produtos/{produto_id}', response_model=schemas.Produto)
def busca_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()


    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return produto



#ROTA ATUALIZAR PRODUTO
@app.put("/atualizar_produto/{produto_id}", response_model=schemas.Produto)
def atualizar_produto(
    produto_id: int,
    produto: schemas.ProdutoCreate,
    db: Session = Depends(get_db)
):

    produto_db = db.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()

    if not produto_db:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produto_db.titulo = produto.titulo
    produto_db.preco = produto.preco
    produto_db.descricao = produto.descricao

    db.commit()
    db.refresh(produto_db)

    return produto_db

#ROTA DELETA PRODUTO
@app.delete('/produtos/{produto_id}')
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):

    produto = db.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    db.delete(produto)
    db.commit()


    return {"mensagem": "Produto deletado com sucesso"}