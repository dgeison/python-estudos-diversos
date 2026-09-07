from array import array


def importa_lista(arquivo):
    lista = []
    with open(arquivo) as tf:
        lines = tf.read().split('","')
    for line in lines:
        lista.append(line)
    return lista


def ordena(lista):
    tamanho_da_lista = len(lista) - 1

    for posicao_atual in range(0, tamanho_da_lista):
        posicao_menor = posicao_atual
        menor_nome = lista[posicao_menor]

        for posicao_busca in range(posicao_atual, tamanho_da_lista):
            nome_busca = lista[posicao_busca + 1]

            if menor_nome > nome_busca:
                menor_nome = nome_busca
                posicao_menor = posicao_busca + 1

        if posicao_menor != posicao_atual:
            menor_nome = lista[posicao_menor]
            lista[posicao_menor] = lista[posicao_atual]
            lista[posicao_atual] = menor_nome

    return lista


def main():
    lista_de_alunos = ["Brendo", "Erica", "Monica", "Nico", "Paulo", "Rodrigo", "Wanessa"]

    for nome in lista_de_alunos:
        print(nome)

if __name__ == "__main__":
    main()