import matplotlib.pyplot as plt
import numpy as np

# Define os pontos de controle
P0 = np.array([0, 0])
P1 = np.array([1, 1])
P2 = np.array([1, 0])
P3 = np.array([2, 1])

# Define a função para calcular a curva cúbica de Bézier
def bezierCubico(t, P0, P1, P2, P3):

    #Define a expressão genérica da curva de cúbica de Bézier usando o triângulo de Pascal
    # np.outer - calcula o produto externo de dois vetores
    expressao = np.outer((1-t)**3, P0) + 3*np.outer(t*(1-t)**2, P1) + 3*np.outer(t**2*(1-t), P2) + np.outer(t**3, P3)

    return expressao

# Calcula os valores de x e y para cada valor de t no intervalo [0, 1]
t = np.linspace(0, 1, num=100)
x, y = bezierCubico(t, P0, P1, P2, P3).T

# Plota os pontos resultantes
plt.plot(x, y)

# Marca os pontos de controle no gráfico
plt.plot(P0[0], P0[1], 'ro')
plt.plot(P1[0], P1[1], 'ro')
plt.plot(P2[0], P2[1], 'ro')
plt.plot(P3[0], P3[1], 'ro')

# Desenha uma linha reta entre os pontos de controle
plt.plot([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], 'r-')

# Adiciona rótulos para cada ponto de controle
plt.text(P0[0]+0.05, P0[1]+0.05, 'P0')
plt.text(P1[0]+0.05, P1[1]+0.05, 'P1')
plt.text(P2[0]+0.05, P2[1]+0.05, 'P2')
plt.text(P3[0]+0.05, P3[1]+0.05, 'P3')


plt.show()