# # Importa o módulo 'veiculos' (o ficheiro veiculos.py)
# import veiculos

# # Para usar as classes, temos de dizer AO PYTHON ONDE encontrá-las:
# # [nome_do_modulo].[nome_da_classe]
# meu_carro = veiculos.Carro("Ford", "Azul")
# meu_tesla = veiculos.CarroEletrico("Tesla", "Branco", 75)

# meu_carro.ligar()
# meu_tesla.ligar()


# Do módulo 'veiculos', importa as classes Carro e CarroEletrico
from veiculos import Carro, CarroEletrico

# Agora, podemos usar as classes diretamente!
meu_carro = Carro("Ford", "Azul")
meu_tesla = CarroEletrico("Tesla", "Branco", 75)

meu_carro.ligar()
meu_tesla.ligar()