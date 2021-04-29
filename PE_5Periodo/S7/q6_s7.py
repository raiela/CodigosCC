try:
    # Importando dependências necessárias
    import numpy as np
    import matplotlib.pyplot as plt

except:

    print("Falta instalaçao de dependencias")

# Função para plot
def q6_graphing():
    
    # Variáveis contendo uma lista para os valores de x, y e z
    x_data = []
    y_data = []
    z_data = []
    
    # Abrindo o arquivo
    arq = open('datas/data_q6.txt', 'r')
    
    # Percorrendo o arquivo
    for line in arq.readlines():
        
        # Salvando cada valor de uma linha em uma variável
        a,x,y,z = line.split()
        x_data.append(float(x))
        y_data.append(float(y))
        z_data.append(float(z))
    
    # Plotando o gráfico
    plt.plot(x_data, color='red')
    plt.plot(y_data, color='blue')
    plt.plot(z_data, color='green')

    plt.xlabel('Position within chromosome')
    plt.legend(['Mut1', 'Mut2', 'Mut3'], bbox_to_anchor=(0.2,1), loc='upper right')
    plt.ylabel('Value')

    plt.show()
    
q6_graphing()