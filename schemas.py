from pydantic import BaseModel

#ESTRUTURA BASICA
class ProdutoBase(BaseModel):
    titulo: str
    preco: float
    descricao: str

#USADO PARA CRIAR PRODUTO
class ProdutoCreate(ProdutoBase):
    pass

#USADO PARA RESPOSTA DAD API
class Produto(ProdutoBase):
    id: int


class Config:
    from_attributes = True
