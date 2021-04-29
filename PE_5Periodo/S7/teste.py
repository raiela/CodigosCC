import numpy as np
import matplotlib.pyplot as plt
    
x = [1, 2, 3]
y = [10, 20, 30]
y2 = [15, 10, 40] # valores do eixo
y3 = [20, 10, 35] # eixo
yBar = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
z = [i * 5 for i in yBar]
xBar = range(len(yBar))
azul = "blue"
verde = "green"
preto = "black"

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Título do gráfico')
plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()
    