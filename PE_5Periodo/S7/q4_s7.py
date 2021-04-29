try: 
    
    # Importando pacotes necessários
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt

except:
    
    print("Falta instalaçao de dependencias")

# Definindo os valores de y
def data_y():
    
    x = [2,1,2,3,3,6,5,10,9,18]
    return x

# Definindo os valores de y
def data_x():
    
    y = ['D1 Male','D1 Female','D2 Male','D2 Female','D3 Male','D3 Female','D4 Male','D4 Female','D5 Male','D5 Female']
    return y

# Função responsável por plotar o gráfico
def q4_graphing():
    
    # Definindo os valores do gráfico
    fig, ax = plt.subplots(figsize=(10,5))
    graph1 = ax.bar(data_x(), data_y(), edgecolor='k', color=['red','orange','yellow','green','lime', 'turquoise','#1E90FF','darkblue','purple','#FF00FF'], width=0.7)
    
    # Legendas de cada barra no eixo X
    plt.xticks(data_x())
    plt.yticks([0, 5, 10, 15])
    plt.xticks(fontsize=8)
    plt.box(False)
    
    # Plotar
    plt.show()
    

q4_graphing()