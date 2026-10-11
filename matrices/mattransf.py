import numpy as np
import matplotlib.pyplot as plt

# Matriz 'M'
M = np.array([[0,0.5,1,0], [0,1,0,0]]) # Triángulo con altura de 1

# Matrices de transformación 'A'
# A = np.array([1,0],[0,1]) - Matriz de identidadd

# Lo hace más delgado y más alto
A1 = np.array([[0.5,0],[0,2]])

# Matriz para reflejar
A2 = np.array([[1,0],[0,-1]])

# Matriz para rotar
theta = np.pi / 4
A3 = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# Multiplicación de matrices
# W = np.matmul(A1, M)
# W = np.matmul(A2,np.matmul(A1,M))
W = np.matmul(A3, np.matmul(A2, np.matmul(A1, M)))

plt.plot(W[0], W[1], '-o')
plt.axis('equal')
plt.show()