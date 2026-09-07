# Pesquisa binária em Python

# suponha que você tenha uma lista de 128 nomwas, e está procurando por um nome em particular. Qual é o máximo de passos que você terá que dar na pesquisa binária?

# 7 passos
# 128 / 2 = 64 ...


# suponha que você tenha uma lista de 256 nomes. Qual é o máximo de passos que você terá que dar?

# 8 passos
# 256 / 2 = 128 ...

# O(log n) é o tempo de execução da pesquisa binária
# O(log 128) = 7
# O(log 256) = 8


# O(log n) é mais rápido que O(n) (tempo de execução da pesquisa linear)


def base_binaria(item, minha_lista):
    """
    Realiza uma pesquisa binária em uma lista ordenada.

    Args:
        item (any): O item a ser procurado na lista.
        minha_lista (list): A lista ordenada onde a pesquisa será realizada.

    Returns:
        int: O índice do item na lista, se encontrado. Caso contrário, retorna None.

    """
    item_1 = 0  # Define o início da lista
    item_2 = len(minha_lista) - 1  # Define o final da lista
    passos = 0

    while (item_1 <= item_2):  # Continua a busca enquanto o início for menor ou igual ao final
        meio_da_lista = (item_1 + item_2) // 2  # Encontra o meio da lista
        chute = minha_lista[meio_da_lista]  # O chute é o valor no meio da lista

        if chute == item:  # Se o chute for igual ao item procurado
            return meio_da_lista, passos  # Retorna o índice do item e o número de passos
        if chute > item:  # Se o chute for maior que o item
            item_2 = meio_da_lista - 1  # Move o final para o meio da lista - 1
        else:  # Se o chute for menor que o item
            item_1 = meio_da_lista + 1  # Move o início para o meio da lista + 1
        passos += 1

    return None, passos # Retorna None e o número de passos se o item não estiver na lista


# minha_lista = [1, 3, 5, 7, 9]

# print(base_binaria(3, minha_lista))
# print(base_binaria(-1, minha_lista))
# print(base_binaria(11, minha_lista))


# minha_lista = list(range(128))

# print(base_binaria(0, minha_lista))
# print(base_binaria(127, minha_lista))
# print(base_binaria(64, minha_lista))
# print(base_binaria(63, minha_lista))
# print(base_binaria(18, minha_lista))
# print(base_binaria(75, minha_lista))
# print(base_binaria(256, minha_lista))
# print(base_binaria(-1, minha_lista))
# print(base_binaria(89, minha_lista))

minha_lista = ['Adam', 'Benjamin', 'Chloe', 'Daniel', 'Ella', 'Frank', 'Grace', 'Henry', 'Isabella', 'Jack', 'Kate', 'Liam', 'Mia', 'Noah', 'Olivia', 'Parker', 'Quinn', 'Ryan', 'Sophia', 'Thomas', 'Uma', 'Victoria', 'William', 'Xavier', 'Yara', 'Zachary']


print(base_binaria('Alice', minha_lista))
print(base_binaria('Zachary', minha_lista))
print(base_binaria('Jack', minha_lista))
print(base_binaria('Isabella', minha_lista))
print(base_binaria('Benjamin', minha_lista))
print(base_binaria('Olivia', minha_lista))

