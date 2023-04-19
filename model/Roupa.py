from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Roupa(Base):
    __tablename__ = 'roupa'

    id = Column("pk_roupa", Integer, primary_key=True)
    categoria = Column(String(140))
    quantidade = Column(Integer)
    valor = Column(Float)
    tamanho = Column(String(3))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, categoria:str, tamanho:str, quantidade:int, valor:float,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Roupa

        Arguments:
            Categoria: tipo da roupa.
            quantidade: quantidade que se espera comprar daquela roupa
            tamanho: tamanho da roupa
            valor: valor esperado para a roupa
            data_insercao: data de quando a roupa foi inserida à base
        """
        self.categoria = categoria
        self.quantidade = quantidade
        self.valor = valor
        self.tamanho = tamanho 

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
