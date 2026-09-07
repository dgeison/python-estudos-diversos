# API - É um lugar para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo- Criar uma API que disponibilize a consulta, criação, edição e exclusão de livros.
# 2. URL base - localhost
# 3. endpoints -
#     - localhost/livros (GET)
#     - localhost/livros/id (GET)
#     - localhost/livro/id (PUT)
#     - localhost/livro/id (DELETE)
# 4. Quais recursos - Livros


from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "O Senhor dos Anéis - A Sociedade do Anel",
        "autor": "J. R. R. Tolkien",
    },
    {
        "id": 2,
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J. K. Rowling",
    },
    {
        "id": 3,
        "titulo": "Harry Potter e o Prisioneiro de Azkaban",
        "autor": "J. K. Rowling",
    },
]


# {
#     "id": 4,
#     "titulo": "Harry Potter e o Prisioneiro de Azkaban",
#     "autor": "J. K. Rowling",
# }

# consultar (todos)


@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)


# consultar (id)
@app.route("/livros/<int:id>", methods=["GET"])
def obter_livro(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)
    return jsonify({"erro": "livro nao encontrado"}), 404


# Editar
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return jsonify({"erro": "livro nao encontrado"}), 404


# Criar
@app.route("/livros", methods=["POST"])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201


# Excluir
@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros.pop(indice)
            return jsonify(livros)
    return jsonify({"erro": "livro nao encontrado"}), 404


app.run(port=5000, host="localhost", debug=True)
