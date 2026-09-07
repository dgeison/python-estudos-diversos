import os

# Coordenadas do aeroporto LAX (Los Angeles)
lax_coordinates = (33.9425, -118.408056)
print(f"Tupla original: {lax_coordinates}")

# Desempacotamento da tupla em variáveis separadas
latitude, longitude = lax_coordinates
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

# Exemplo de divmod: retorna quociente e resto da divisão
print(f"\ndivmod(20, 8): {divmod(20, 8)}")

# Usando desempacotamento com * para passar elementos da tupla como argumentos
t = (20, 8)
print(f"divmod(*t) onde t = {t}: {divmod(*t)}")

# Desempacotando o resultado diretamente em variáveis
quotient, remainder = divmod(*t)
print(f"Quociente: {quotient}, Resto: {remainder}")

# Exemplo de desempacotamento ignorando valores indesejados com _
# Usando os.path.split() para separar o caminho do nome do arquivo
caminho_completo = '/home/luciano/.ssh/id_rsa.pub'
_, filename = os.path.split(caminho_completo)
print(f"\nCaminho completo: {caminho_completo}")
print(f"Nome do arquivo (ignorando o diretório): {filename}")

caminho = '/home/user/arquivo.txt'

# Divide diretório e arquivo
os.path.split(caminho)      # ('/home/user', 'arquivo.txt')

# Pega só o nome do arquivo
os.path.basename(caminho)   # 'arquivo.txt'

# Pega só o diretório
os.path.dirname(caminho)    # '/home/user'

# Divide nome e extensão
os.path.splitext(caminho)   # ('/home/user/arquivo', '.txt')

print()

# Desempacotamento com * (unpacking extendido) - Python 3+
# O * captura múltiplos elementos em uma lista

# Exemplo 1: capturando os elementos restantes
a, b, *rest = range(5)
print(f"a={a}, b={b}, rest={rest}")  # a=0, b=1, rest=[2, 3, 4]

# Exemplo 2: com menos elementos
a, b, *rest = range(3)
print(f"a={a}, b={b}, rest={rest}")  # a=0, b=1, rest=[2]

# Exemplo 3: sem elementos restantes
a, b, *rest = range(2)
print(f"a={a}, b={b}, rest={rest}")  # a=0, b=1, rest=[]

# O * também pode aparecer em outras posições
*inicio, penultimo, ultimo = range(5)
print(f"inicio={inicio}, penultimo={penultimo}, ultimo={ultimo}")  # inicio=[0, 1, 2], penultimo=3, ultimo=4

# Ou no meio da atribuição
primeiro, *meio, ultimo = range(5)
print(f"primeiro={primeiro}, meio={meio}, ultimo={ultimo}")  # primeiro=0, meio=[1, 2, 3], ultimo=4