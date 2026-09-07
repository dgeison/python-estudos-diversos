from typing import Optional
from itertools import count
from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel, Field
from tinydb import TinyDB, Query


server = Flask(__name__)
spec = FlaskPydanticSpec("flask", title="Flask API", version="1.0.0")
spec.register(server)
database = TinyDB("db.json")
c = count()


class QueryPessoa(BaseModel):
    id: Optional[int]
    nome: Optional[str]
    idade: Optional[int]


class Pessoa(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    nome: str
    idade: int


class Pessoas(BaseModel):
    pessoas: list[Pessoa]
    count: int


@server.get("/pessoas")
@spec.validate(query=QueryPessoa, resp=Response(HTTP_200=Pessoas))
def buscar_pessoas():
    """Retorna todas as pessoas cadastradas no banco de dados"""
    query = request.context.query.dict(exclude_none=True)
    todas_as_pessoas = database.search(Query().fragment(query))
    return jsonify(
        Pessoas(
            pessoas=todas_as_pessoas,
            count=len(todas_as_pessoas),
        ).dict()
    )


@server.get("/pessoas/<int:id>")
@spec.validate(resp=Response(HTTP_200=Pessoa))
def buscar_pessoa(id):
    """Retorna todas as Pessoas da base de dados."""
    try:
        pessoa = database.search(Query().id == id)[0]
    except IndexError:
        return {"message": "Pessoa não encontrada"}, 404
    return jsonify(pessoa)


@server.put("/pessoas/<int:id>")
@spec.validate(
    body=Request(Pessoa),
    resp=Response(HTTP_200=Pessoa),
)
def alterar_pessoa(id: int):
    """Altera uma pessoa na base de dados"""
    Pessoa = Query()
    body = request.context.body.dict()
    database.update(body, Pessoa.id == id)
    return jsonify(body)


@server.delete("/pessoas/<int:id>")
@spec.validate(resp=Response("HTTP_204"))
def delete_pessoa(id: int):
    """Deleta uma pessoa da base de dados"""
    Pessoa = Query()
    database.remove(Pessoa.id == id)
    return jsonify({})


@server.post("/pessoas")
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_201=Pessoa))
def inserir_pesssoas():
    """Insere uma pessoa na base de dados"""
    body = request.context.body.dict()
    database.insert(body)
    return body


server.run()
