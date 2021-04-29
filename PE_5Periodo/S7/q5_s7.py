try:
    # Importando dependências necessárias
    import numpy as np
    import matplotlib.pyplot as plt

except:
    print("Falta instalaçao de dependencias")

def q5_graphing():
    
    # Definindo as variáveis
    gene_data = []
    state_data = []
    x_dataUP = []
    x_dataDOWN = []
    
    y_dataUP = []
    y_dataDOWN = []
    
    x_unchanging = []
    y_unchanging = []    
        
    # Abrindo o arquivo. Para esse código funcionar a questão tem que ser rodada de dendro do diretorio pe-s7        
    arq = open('datas/data_q5.txt', 'r')
    
    # Percorrendo cada linha do arquivo
    for line in arq.readlines():
    
        # Dividindo cada coluna da linha em uma variável
        g,x,y,z = line.split()
        
        # Fazendo as verificações para salvar os dados nas variáveis correspondentes
        if (z == "up"):
        
            x_dataUP.append(float(x))
            y_dataUP.append(float(y))
        
        elif(z == "down"):
        
            x_dataDOWN.append(float(x))
            y_dataDOWN.append(float(y))
        
        elif(z == 'unchanging'):
        
            x_unchanging.append(float(x))
            y_unchanging.append(float(y))
            
        gene_data.append(g)
        state_data.append(z)

    # Plotando subgráficos para formar uma imagem só
    fig, ax = plt.subplots()
    # Definindo os valores
    ax.scatter(x_dataUP, y_dataUP, color='red')
    ax.scatter(x_dataDOWN, y_dataDOWN, color='blue')
    ax.scatter(x_unchanging, y_unchanging, color='gray')
    
    plt.yticks([0, 5, 10])
    plt.xticks([0, 5, 10])
    plt.xlabel('Condition1')
    plt.ylabel('Condition1')
    
    plt.show()

q5_graphing()

