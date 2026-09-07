# Exemplos de fatiamento (slicing) de listas
l = [10, 20, 30, 40, 50, 60]

# Fatiamento [:2] - retorna elementos do início até o índice 2 (exclusivo)
print(l[:2])  # split at 2
# [10, 20]

# Fatiamento [2:] - retorna elementos do índice 2 até o final
print(l[2:])
# [30, 40, 50, 60]

# Fatiamento [:3] - retorna elementos do início até o índice 3 (exclusivo)
print(l[:3])  # split at 3
# [10, 20, 30]

# Fatiamento [3:] - retorna elementos do índice 3 até o final
print(l[3:])
# [40, 50, 60]

# Exemplos de fatiamento com step (passo)
s = 'bicycle'

# Fatiamento [::3] - retorna caracteres pulando de 3 em 3
print(s[::3])
# 'bye'

# Fatiamento [::-1] - retorna a string invertida (passo negativo)
print(s[::-1])
# 'elcycib'

# Fatiamento [::-2] - retorna a string invertida pulando de 2 em 2
print(s[::-2])
# 'eccb'

print()

# Exemplo prático: fatiamento de invoice (nota fiscal)
# Usando slices nomeados para melhorar a legibilidade do código
invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""

# Definindo slices nomeados para cada campo da invoice
SKU = slice(0, 6)           # Código do produto
DESCRIPTION = slice(6, 40)  # Descrição do produto
UNIT_PRICE = slice(40, 52)  # Preço unitário
QUANTITY = slice(52, 55)    # Quantidade
ITEM_TOTAL = slice(55, None)  # Total do item

# Separando as linhas e ignorando as duas primeiras (cabeçalho)
line_items = invoice.split('\n')[2:]

# Iterando sobre cada item e imprimindo preço e descrição
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])
# Saída:
#     $17.50   Pimoroni PiBrella
#      $4.95   6mm Tactile Switch x20
#     $28.00   Panavise Jr. - PV-201
#     $34.95   PiTFT Mini Kit 320x240


