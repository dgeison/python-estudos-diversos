# Coordenadas geográficas (latitude, longitude)
lax_coordinates = (33.9425, -118.408056)

# Dados de uma cidade (nome, ano, população, mudança, área)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)

# Exibe os dados da cidade
print(f"Cidade: {city}")
print(f"Ano: {year}")
print(f"População: {pop:,}")
print(f"Mudança: {chg}%")
print(f"Área: {area} km²")
print()

# Lista de passaportes (país, número)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# Exibe passaportes ordenados
print("Passaportes ordenados:")
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
print()

# Exibe apenas os países (ignorando números com _)
print("Países:")
for country, _ in traveler_ids:
    print(country)

print()

# Exemplo: Tuplas com objetos mutáveis
# Tuplas são imutáveis, mas podem conter objetos mutáveis (como listas)
print("Exemplo de tuplas com objetos mutáveis:")
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
print(f"a == b: {a == b}")  # True - tuplas são iguais inicialmente

# Modifica a lista dentro da tupla b
b[-1].append(99)
print(f"Após b[-1].append(99):")
print(f"a == b: {a == b}")  # False - tuplas agora são diferentes
print(f"a = {a}")
print(f"b = {b}")

print()

# Função para verificar se um objeto é hashable (imutável)
def fixed(o):
    """Verifica se um objeto é hashable (pode ser usado como chave de dicionário)"""
    try:
        hash(o)
    except TypeError:
        return False
    return True

# Tupla com objetos imutáveis (hashable)
tf = (10, 'alpha', (1, 2))
# Tupla com objeto mutável - lista (não é hashable)
tm = (10, 'alpha', [1, 2])

print("Verificando se tuplas são hashable:")
print(f"tf = {tf}")
print(f"fixed(tf): {fixed(tf)}")  # True - todos os elementos são imutáveis
print()
print(f"tm = {tm}")
print(f"fixed(tm): {fixed(tm)}")  # False - contém uma lista (mutável)