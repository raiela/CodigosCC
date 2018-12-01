lista = list(map(int, input("Digite a lista: ").split()))

for i in range(1, len(lista)):

    j = i

    while j > 0 and lista[j] < lista[j-1]:
        lista[j],lista[j-1] = lista[j-1],lista[j]
        j -= 1

print(lista)