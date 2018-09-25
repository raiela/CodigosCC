lista = [3, 1, 4, 5, 6, 9, 8, 1, 2]
l = []
menor = lista[0]
aux = 0
cont = 0
print(lista)
for i in range(len(lista)):
	for k in range(len(lista)):
		if(lista[i] <= lista[k]):
			aux = lista[k]
			lista[k] = lista[i]
			lista[i] = aux

print(lista)



