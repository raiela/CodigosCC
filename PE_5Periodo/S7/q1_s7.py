# exceção criada para relembrar de baixar a biblioteca em caso de já não estar instalada no PC. Se o código nao rodar, entrará nessa exceção
# Está sendo sugerido que se baixe as dependências da biblioteca par que o código possa rodar
try: 
    
    # pacotes necessários
    import matplotlib.pyplot as plt

except:
    
    print("Baixa a biblioteca matplotlib")

# variáveis de x
def data_x_ages():
    
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    return x

# variáveis de y
def data_y_weight():

    y = [3.6, 4.4, 5.2, 6, 6.6, 7.2, 7.8, 8.4, 8.8, 9.2]

    return y

# função que plotará o gráfico
def q1_graphing():

    # editanto a parte visual dos gráfico
    # o atribudo markerfacecolor deixa os pontos do grafico com cor branca
    plt.plot(data_x_ages(),data_y_weight(), 
             marker='o', 
             color='k',
             markerfacecolor='white')
    
    # definindo a legenda para os eixos x e y
    plt.xlabel("Age (Months)")
    plt.ylabel("Weight (kg)")
    
    # titulo do gráfico
    plt.title("The relationship between age and weight in a growing infant")
    
    plt.show()

q1_graphing()