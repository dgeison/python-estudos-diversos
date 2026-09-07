class Cachorro:
    # Este é o método "construtor"
    def __init__(self, nome, raca):
        print("Um novo cachorro foi criado!")
        self.nome = nome
        self.raca = raca

    # Este é um método
    def latir(self):
        print(f"{self.nome} diz: Au au!")

    # Como seria o método 'apresentar' aqui?
    def apresentar(self):
        print(f"Eu sou {self.nome}, um {self.raca}")


# Exemplo de uso da classe Cachorro
# Criando o cachorro Rex
rex = Cachorro("Rex", "Pastor Alemão")

# Criando o cachorro Bobby
bobby = Cachorro("Bobby", "Vira-lata")


rex.latir()

bobby.latir() # O python transforma isso em Cachorro.latir(bobby)


# rex.apresentar()