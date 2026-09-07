class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
    
    def ligar(self):
        print(f"O {self.marca} está ligando. (Vrum vrum!)")
    
    # ... outros métodos ...

class CarroEletrico(Carro):
    def __init__(self, marca, cor, bateria_kwh):
        super().__init__(marca, cor)
        self.bateria_kwh = bateria_kwh

    def ligar(self):
        super().ligar()
        print("Verificando sistemas elétricos.")
    
    # ... outros métodos ...