from array import array


def importa_lista(arquivo):
    lista = []
    with open(arquivo) as tf:
        lines = tf.read().split('","')
    for line in lines:
        lista.append(line)
    return lista


def ordena(lista):
    tamanho_da_lista = len(lista)
    lista_temporaria = [0] * tamanho_da_lista
    merge_sort(lista, lista_temporaria, 0, tamanho_da_lista - 1)


def merge_sort(lista, lista_temporaria, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        merge_sort(lista, lista_temporaria, inicio, meio)

        merge_sort(lista, lista_temporaria, meio + 1, fim)

        merge(lista, lista_temporaria, inicio, meio + 1, fim)


def merge(lista, lista_temporaria, inicio, meio, fim):
    fim_primeira_parte = meio - 1
    indice_temporario = inicio
    tamanho_da_lista = fim - inicio + 1

    while inicio <= fim_primeira_parte and meio <= fim:
        if lista[inicio] <= lista[meio]:
            lista_temporaria[indice_temporario] = lista[inicio]
            inicio += 1
        else:
            lista_temporaria[indice_temporario] = lista[meio]
            meio += 1
        indice_temporario += 1

    while inicio <= fim_primeira_parte:
        lista_temporaria[indice_temporario] = lista[inicio]
        indice_temporario += 1
        inicio += 1

    while meio <= fim:
        lista_temporaria[indice_temporario] = lista[meio]
        indice_temporario += 1
        meio += 1

    for i in range(0, tamanho_da_lista):
        lista[fim] = lista_temporaria[fim]
        fim -= 1


def main():
    lista_de_alunos = importa_lista('../data/lista_alunos')

    ordena(lista_de_alunos)

    for nome in lista_de_alunos:
        print(nome)

if __name__ == "__main__":
    main()