try:
    # Importando dependências necessárias
    import numpy as np
    import matplotlib.pyplot as plt

except:
    print("Falta instalaçao de dependencias")


def q3_graphing():

    # Definindo valores para a geração dos gráficos
    graph1_values =  np.random.normal(loc=0,scale=1,size=10000)
    graph2_values =  np.random.normal(loc=4,scale=1,size=10000)
    
    # Concatenando os valores dos dois gráficos para gerar juntos
    finalGraph = np.concatenate((graph1_values, graph2_values))

    # Editando a aparência e plotando o gráfico
    plt.hist(finalGraph, color='k', bins=110, edgecolor='k', facecolor='white')
    
    # Retirando o quadrado delimitando o plot do gráfico
    plt.box(False)
    
    # Título e legenda para os eixos
    plt.title('Mixed distribution histogram')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.show()

q3_graphing()