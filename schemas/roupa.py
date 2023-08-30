from pydantic import BaseModel
from typing import Optional, List
from model.Roupa import Roupa



class RoupaSchema(BaseModel):
    """ Define como uma nova roupa a ser inserido deve ser representado
    """
    categoria: str = "Camisa"
    quantidade: int = 5
    tamanho: str = "M"
    valor: float = 20

class RoupaEditSchema(BaseModel):
    """ Define como uma roupa é editada
    """
    categoria: str = "Camisa"
    quantidade: int = 5
    tamanho: str = "M"
    valor: float = 20
    id: int = 1

class RoupaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base id da roupa.
    """
    id: int = 1


class ListagemRoupasSchema(BaseModel):
    """ Define como uma listagem de roupas será retornada.
    """
    roupas:List[RoupaSchema]


def apresenta_roupas(roupas: List[Roupa]):
    """ Retorna uma representação da roupa seguindo o schema definido em
        RoupaViewSchema.
    """
    result = []
    for roupa in roupas:
        result.append({
            "id": roupa.id,
            "categoria": roupa.categoria,
            "quantidade": roupa.quantidade,
            "tamanho": roupa.tamanho,
            "valor": roupa.valor,
        })

    return {"roupas": result}


class RoupaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: str

class RoupaViewSchema(BaseModel):
    """ Define como uma roupa será retornada: roupa.
    """
    id: int = 1
    categoria: str = "Camisa"
    quantidade: int = 5
    tamanho: str = "M"
    valor: float = 20

def apresenta_roupa(roupa: Roupa):
    """ Retorna uma representação da roupa seguindo o schema definido em
        RoupaViewSchema.
    """
    return {
        "id": roupa.id,
        "categoria": roupa.categoria,
        "quantidade": roupa.quantidade,
        "tamanho": roupa.tamanho,
        "valor": roupa.valor
    }
 

