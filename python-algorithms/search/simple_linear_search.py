from array import array


def busca(lista, nome_pesquisado):
    tamanho_da_lista = len(lista)
    for atual in range(0, tamanho_da_lista):
        if (lista[atual] == nome_pesquisado):
            return atual

    return -1


def main():
    lista_de_alunos = ["Brendo", "Erica", "Monica", "Nico", "Paulo", "Rodrigo", "Wanessa"]
    posicao_do_aluno = busca(lista_de_alunos, "Wanessa")
    print("Aluno(a) {} está na posição {}".format(lista_de_alunos[posicao_do_aluno], posicao_do_aluno))


if __name__ == "__main__":
    main()