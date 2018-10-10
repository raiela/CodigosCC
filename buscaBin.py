'''OBS.: Uma busca binária só funciona quando a lista está ordenada'''

def buscaBinaria(n, lista):
    meio = len(lista)//2
    if n == lista[meio]:
        return True
    elif meio == 0:
        return False


    elif n < lista[meio]:
        return buscaBinaria(n, lista[:meio])
    else:
        return buscaBinaria(n, lista[meio+1:])

lista = list(map(int, input("Digite a lista: ").split()))
n = int(input("Digite o valor que quer verificiar: "))
lista.sort()
print(buscaBinaria(n, lista))
