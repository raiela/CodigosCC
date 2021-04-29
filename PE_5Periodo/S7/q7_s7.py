try:
    # Importando dependências necessárias
    import numpy as np
    import matplotlib.pyplot as plt

except:

    print("Falta instalaçao de dependencias")
    

# Definindo a função de plot
def q7_graphing():

    # Abrindo o arquvivo
    arq = open('datas/data_q7.txt', 'r')
    
    # Percorrendo cada linha    
    for line in arq.readlines():

        # Salvando os valores da linha em variáveis
        a,x,y,z,t = line.split()

        # modificando os types dessas variáveis
        text = str(a)
        y_position = float(x)
        x_position = float(y)
        x_error = float(t)
        y_error = float(z)
        
        # PLotando
        plt.errorbar(x_position, y_position, yerr = y_error, xerr = x_error, marker='d', color = 'k', capsize=4)
        plt.text((x_position-0.15), (y_position-0.3), s=text,fontdict=dict(size=6))  
        
    plt.xlabel('Brain Weight')
    plt.yticks([-1, 0, 1, 2, 3, 4, 5])
    plt.xticks([0, 1, 2, 3])
    plt.ylabel('Body Weight')
    plt.show()
        
        
        
        
q7_graphing()