# 1. Definição da Classe
class Carro:
    # 2. O Construtor: Como preenchemos os ???
    def __init__(self, marca, cor):
        # Como guardamos a marca e a cor?
        self.marca = marca
        self.cor = cor

    # 3. O Método 'ligar'
    def ligar(self):
        # Como acessamos a marca do carro específico?
        print(f"O {self.marca} está ligando.")

    # 4. O Método 'buzinar'
    def buzinar(self):
        print("Bip bip!")

    # 5. O Método 'mostrar_cor' (opcional)
    def mostrar_cor(self):
        print(f"A cor do carro é {self.cor}.")


# --- Código para testar ---

# Criando um objeto 'Carro'
# meu_carro = Carro("Ford", "Azul")

# Chamando os métodos do objeto
# meu_carro.ligar()   # Saída esperada: O Ford está ligando.
# meu_carro.buzinar() # Saída esperada: Bip bip!
# meu_carro.mostrar_cor() # Saída esperada: A cor do carro é Azul.


class CarroEletrico(Carro):
    # O init da filha recebe mais um argumento
    def __init__(self, marca, cor, bateria_kwh):
        print("Inicializando CarroEletrico")

        # 1. Chamando o init da classe mãe
        super().__init__(marca, cor)

        self.bateria_kwh = bateria_kwh

    def carregar_bateria(self):
        print(f"O {self.marca} está carregando a bateria.")

    def ligar(self):
        # print(f"O {self.marca} está ligando silenciosamente.")
        super().ligar()

        print("Verificando sistemas elétricos...")


# Criando um CarroEletrico
# Repare que ele usa o __init__ da classe Carro!
# meu_tesla = CarroEletrico("Tesla", "Branco")

# Chamando métodos que o CarroEletrico "herdou"
# meu_tesla.ligar()
# meu_tesla.buzinar()
# meu_tesla.carregar_bateria()
# meu_tesla.ligar()


# meu_fusca = Carro("VW", "Azul")
meu_tesla = CarroEletrico("Tesla", "Branco", 75)

# print("--- Ações do Fusca ---")
# meu_fusca.ligar()

# print("\n--- Ações do Tesla ---")
# meu_tesla.ligar()
# meu_tesla.carregar_bateria()


print(f"\nMarca: {meu_tesla.marca}") # Definido pelo __init__ do Carro
print(f"Bateria: {meu_tesla.bateria_kwh}") # Definido pelo __init__ do CarroEletrico
meu_tesla.ligar()