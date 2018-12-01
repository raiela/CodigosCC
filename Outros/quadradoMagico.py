'''Um quadrado magico é uma matriz cuja a soma das linhas, colunas e diagonais são a mesma'''

def quadradoMagico(lista):
    flag = True
    flagGeral = True
    diagonal1 = 0
    diagonal2 = 0
    coluna = []
    linha = []
    aux = len(matriz)-1
    for i in range(len(matriz)):
        c = 0
        l = 0
        for j in range(len(matriz)):
            l += matriz[i][j]
            c += matriz[j][i]
        diagonal1 += matriz[i][i]
        diagonal2 += matriz[i][aux]
        linha.append(l)
        coluna.append(c)
        aux -= 1

    for i in range(len(linha)):
        for j in range(len(linha)):
            if(linha[i] != linha[j]):
                flag = False
                break
            if(coluna[i] != coluna[j]):
                flag = False
                break
    if(flag == True):
        if(diagonal2 != diagonal2):
            flagGeral = False
    else:
        flagGeral = False

    return flagGeral


matriz =[]

tam = int(input("Digite o tamanho da matriz: "))
for i in range(tam):
    coluna = list(map(int, input().split()))
    matriz.append(coluna)

print(quadradoMagico(matriz))
