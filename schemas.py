from pydantic import BaseModel

class ProdutoBase(BaseModel):
    titulo: str
    preco: float
    descricao: str


class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int


class Config:
    from_attributes = True