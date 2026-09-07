symbols = '$¢£¥€¤'

# Exemplo 1: Gerando uma tupla com os códigos Unicode dos símbolos
result_tuple = tuple(ord(symbol) for symbol in symbols)
print("Tupla com códigos Unicode:")
print(result_tuple)
# Saída: (36, 162, 163, 165, 8364, 164)

# Exemplo 2: Criando um array com os códigos Unicode
import array
result_array = array.array('I', (ord(symbol) for symbol in symbols))
print("\nArray com códigos Unicode:")
print(result_array)
# Saída: array('I', [36, 162, 163, 165, 8364, 164])


# Separador visual entre os exemplos
print('\n' + '-' * 40 + '\n')

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)