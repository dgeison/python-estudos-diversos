import json
from pprint import pprint


# Arquivo de configuração
class ConfigSingleton:
    NOME_ARQUIVO = "config.json"
    _instancia = None

    def __init__(self):
        # Carrega os dados do arquivo de configuração
        with open(self.NOME_ARQUIVO, "r") as f:
            self.dados = json.load(f)

    @classmethod  # método de classe para obter a instância única (isto não está claro pra mim, mas é o que o professor fez)
    def get_instance(cls):
        # equivalente a cls._instancia = ConfigSingleton()
        if cls._instancia is None:
            print("Criando a instância única")
            ConfigSingleton._instancia = (
                ConfigSingleton()
            )  # pra enviar para instancia? Preciso expicações
        return ConfigSingleton._instancia


def main():
    s1 = ConfigSingleton.get_instance()
    s2 = ConfigSingleton.get_instance()
    pprint(s1.dados)
    print(f"s1 is s2: {s1 is s2}")  # Deve imprimir True
    print(f"id(s1): {id(s1)}, id(s2): {id(s2)}")
    s3 = ConfigSingleton()
    print(f"s1 is s3: {s1 is s3}")  # Deve imprimir False


if __name__ == "__main__":
    main()
