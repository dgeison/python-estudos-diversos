# classe "privada"
import json

# classe "privada"
class Singleton:
    def __init__(self):
        print("Criando a instância única")


singleton = Singleton()
dados = None

NOME_ARQUIVO = "config.json"
with open(NOME_ARQUIVO, "r") as arquivo:
    dados = json.load(arquivo)
