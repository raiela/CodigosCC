'''OBS.: Uma busca binária só funciona quando a lista está ordenada'''

def buscaBinaria(n, lista):
    meio = len(lista)//2

    if (len(lista) == 1 and lista[meio] != n):
        return False

    elif n < lista[meio]:
        return buscaBinaria(n, lista[:meio])
    elif n > lista[meio]:
        return buscaBinaria(n, lista[meio+1:])
    else:
        return True

lista = list(map(int, input("Digite a lista: ").split()))
n = int(input("Digite o valor que quer verificiar: "))
lista.sort()
print(buscaBinaria(n, lista))

