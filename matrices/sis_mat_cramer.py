import numpy as np 

A = np.array([
    [2,4,3],
    [0,1,-1],
    [3,5,7]
])

A1 = np.array([
    [6,-4,7], # Reemplazamos con la de resultados para encontrar X1
    [4,1,5],
    [3,-1,7]
])

detA = np.linalg.det(A)

detA1 = np.linalg.det(A1)

X1 = detA1/detA
print(X1)