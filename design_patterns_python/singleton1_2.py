import json
from pprint import pprint


# Arquivo de configuração
class Singleton:
    NOME_ARQUIVO = "config.json"
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Criando nova instância de ConfigSingleton")
            cls._instancia = super().__new__(cls)
            with open(cls.NOME_ARQUIVO, "r") as f:
                cls._instancia.dados = json.load(f)
        return cls._instancia


def main():
    s1 = Singleton()
    pprint(s1.dados)
    s2 = Singleton()
    print(s1 is s2)
    print(id(s1), id(s2))
    s3 = Singleton().__new__(Singleton)  # Força a criação de uma nova instância
    print(s1 is s3)


if __name__ == "__main__":
    main()
