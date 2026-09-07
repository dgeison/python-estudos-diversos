from array import array


def importa_lista(arquivo):
    lista = []
    with open(arquivo) as tf:
        lines = tf.read().split('","')
    for line in lines:
        lista.append(line)
    return lista


def busca(lista, nome_pesquisado):
    tamanho_da_lista = len(lista)
    for atual in range(0, tamanho_da_lista):
        if lista[atual] == nome_pesquisado:
            return atual

    return -1


def main():
    lista_de_alunos = importa_lista('../data/lista_alunos')
    posicao_do_aluno = busca(lista_de_alunos, "Brendo")
    print("Aluno(a) {} está na posição {}".format(lista_de_alunos[posicao_do_aluno], posicao_do_aluno))


if __name__ == "__main__":
    main()