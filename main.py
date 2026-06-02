#CONTROI SISTEMAS QUE RECEBEM REQUISIÇOES
from fastapi import FastAPI, HTTPException
#USADO PARA VALIDAR, ORGANIZAR E TRANSFORMA DADOS AUTOMATICAMENTE
from pydantic import BaseModel
#USADO PARA INDICAR TIPO DE DADOS
from typing import List, Optional

app = FastAPI(title="API ferramentas")

#MODELO DE DADOS
class Ferramenta(BaseModel):
    id:Optional[int] = None
    nome: str
    preco: float
    descricao: str

#LISTA PARA ARMAZENA OBJETOS 
ferramentas: List[Ferramenta] = []


@app.get("/ferramentas", response_model=List[Ferramenta])
async def lista_ferramentas():
    return ferramentas


#ROTA ADICIONAR FERRAMENTA
@app.post("/ferramentas", response_model=Ferramenta, status_code=201)
async def adicionar_ferramenta(ferramenta: Ferramenta):
    ferramenta.id = len(ferramentas) + 1
    ferramentas.append(ferramenta)
    return ferramenta


#ROTA BUSCAR FERRAMENTA POR ID
@app.get("/ferramentas/{ferramenta_id}", response_model=Ferramenta)
async def obter_ferramenta(ferramenta_id: int):
    for f in ferramentas:
        if f.id == ferramenta_id:
            return f
    raise HTTPException(status_code=404, detail="Ferramenta não encontrada")


#ROTA PARA ALTERAR FERRAMENTAS
@app.put("/ferramentas/{ferramenta_id}", response_model=Ferramenta)
async def alterar_ferramenta(ferramenta_id: int, ferramenta_alterada: Ferramenta):
    for index, f in enumerate(ferramentas):
        if f.id == ferramenta_id:
            ferramenta_alterada.id = ferramenta_id

            ferramentas[index] = ferramenta_alterada

            return ferramenta_alterada
        
    raise HTTPException(status_code=404, detail="Ferramenta não encontrada")


#ROTA PARA DELETA
@app.delete("/ferramentas/{ferramenta_id}", status_code=204)
async def deletar_ferramenta(ferramenta_id: int):
    for f in ferramentas:
        if f.id == ferramenta_id:
            ferramentas.remove(f)
            return

    raise HTTPException(
        status_code=404,
        detail="Ferramenta não encontrada"
    )
