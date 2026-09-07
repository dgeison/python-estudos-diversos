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
    inicio = 0
    fim=tamanho_da_lista-1

    while inicio<=fim:
        meio=(inicio+fim)//2
        if lista[meio] == nome_pesquisado:
            return meio
        elif lista[meio] < nome_pesquisado:
            inicio=meio+1
        elif lista[meio] > nome_pesquisado:
            fim = meio-1

    return -1


def main():
    lista_de_alunos = sorted(importa_lista('../data/lista_alunos'))
    for i in range(0,3500):
        posicao_do_aluno = busca(lista_de_alunos, "Zeina")
        print("Aluno(a) {} está na posição {}".format(lista_de_alunos[posicao_do_aluno], posicao_do_aluno))

if __name__ == "__main__":
    main()