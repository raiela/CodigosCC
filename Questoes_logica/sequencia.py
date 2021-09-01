def preencher(n):
    	listaAux = [0]
	for j in range(1, n+1):
		aux = 1
		while aux <= j:
			listaAux.append(j)
			aux += 1
		
	return listaAux

lista = []
maior = -1;
caso = 1
def somar(n):
	soma = 0
	for i in range(n+1):
		soma += i
	
	return soma+1
	
def imprimir(lista, valor):
	print(saida)
	for i in range(valor):
		if i == valor-1:
			print(lista[i], end = "\n\n")
		else:
			print(lista[i], end = " ")
	
while True:
	try:
		ent = int(input())
		if(somar(ent) == 1):
			n = " numero"
		else:
			n = " numeros"
		saida = "Caso "+str(caso)+": "+str(somar(ent))+n;
		if(ent > maior):
			maior = ent;
			lista = preencher(ent)
			imprimir(lista, somar(ent))
		else:
			imprimir(lista, somar(ent))		
		caso += 1
		
	except EOFError:
		break