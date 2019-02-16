lista = list(map(int, input("Digite a lista a ser ordenada: ").split()))

inicio = 1
listaAux = 0

for i in range(len(lista)):
    menor = i

    for j in range(i, len(lista)):
        if(lista[j] < lista[menor]):
            menor = j

    lista[i],lista[menor] = lista[menor],lista[i]

print("Lista ordenada: ",lista)