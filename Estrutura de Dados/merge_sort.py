def merge_sort(lista):
    return divisao(lista)

def divisao(lista):
    meio = len(lista)//2
    if meio == 0:
        return lista
    listaUm = divisao(lista[:meio])
    listaDois = divisao(lista[meio:])
    return combinacao(listaUm, listaDois)

def combinacao(listaUm, listaDois):
    i = j = 0
    lista = []

    for k in range(len(listaUm + listaDois)):
            if i == len(listaUm):
                lista.append(listaDois[j])
                j += 1
            elif j == len(listaDois):
                lista.append(listaUm[i])
                i += 1
            elif listaUm[i] < listaDois[j]:
                lista.append(listaUm[i])
                i += 1
            else:
                lista.append(listaDois[j])
                j += 1

    return lista

lista = [4, 593, 185, 1, -1, -31, -10, 15, 13, 5, 29, 6]
print(merge_sort(lista))