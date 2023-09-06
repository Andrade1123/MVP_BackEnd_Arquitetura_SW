from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect

from model import Session
from model.Roupa import Roupa
from schemas import *


info = Info(title="API de Roupa", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
roupa_tag = Tag(name="Roupa", description="Adição, visualização e remoção de roupas à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/roupa', tags=[roupa_tag],
          responses={"200": RoupaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_roupa(form: RoupaSchema):
    """Adiciona um nova Roupa à base de dados

    Retorna uma representação das roupas.
    """
    roupa = Roupa(
        categoria=form.categoria,
        quantidade=form.quantidade,
        valor=form.valor, tamanho=form.tamanho)
    
    try:
        # criando conexão com a base
        session = Session()
        # adicionando roupa
        session.add(roupa)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return apresenta_roupa(roupa), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Roupa de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        print(e)
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400
    
@app.put('/roupa', tags=[roupa_tag],
          responses={"200": RoupaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def edit_roupa(form: RoupaEditSchema):
    """Editar uma Roupa da base de dados

    Retorna uma representação da roupa.
    """
    roupa = Roupa(
        categoria=form.categoria,
        quantidade=form.quantidade,
        valor=form.valor, tamanho=form.tamanho)
 
    try:
        # criando conexão com a base
        session = Session()
        # Buscando uma roupa e atualizando a base
        roupa_selecionada = session.query(Roupa).filter(Roupa.id == form.id).first()
        roupa_selecionada.categoria = form.categoria
        roupa_selecionada.quantidade = form.quantidade
        roupa_selecionada.valor = form.valor
        roupa_selecionada.tamanho = form.tamanho
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return apresenta_roupa(roupa), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Roupa de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        print(e)
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400



@app.get('/roupas', tags=[roupa_tag],
         responses={"200": ListagemRoupasSchema, "404": ErrorSchema})
def get_roupas():
    """Faz a busca por todos as Roupas cadastradas

    Retorna uma representação da listagem de roupas.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    roupas = session.query(Roupa).all()

    if not roupas:
        # se não há roupas cadastradas
        return {"roupas": []}, 200
    else:
        # retorna a representação de roupas
        print(roupas)
        return apresenta_roupas(roupas), 200

@app.delete('/roupa', tags=[roupa_tag],
            responses={"200": RoupaDelSchema, "404": ErrorSchema})
def del_roupa(query: RoupaBuscaSchema):
    """Deleta uma Roupa a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    id = query.id

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Roupa).filter(Roupa.id == id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Roupa removida da lista", "id":id}
    else:
        # se a roupa não foi encontrada
        error_msg = "Roupa não encontrada na base :/"
        return {"mesage": error_msg}, 404
