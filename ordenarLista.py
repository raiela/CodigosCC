'''Ordenação de um jeito muito pouco eficiente'''

lista = list(map(int, input("Digite a lista a ser ordenada: ").split()))
menor = lista[0]
aux = 0
cont = 0
for i in range(len(lista)):
	for k in range(len(lista)):
		if(lista[i] <= lista[k]):
			aux = lista[k]
			lista[k] = lista[i]
			lista[i] = aux

print(lista)



