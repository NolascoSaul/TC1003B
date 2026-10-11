import numpy as np 

A = np.array([
    [2,4,3],
    [0,1,-1],
    [3,5,7]
])

B = np.array([
    [6],
    [-4],
    [7]
])

det = np.linalg.det(A)

Ainv = np.linalg.inv(A)

X = np.matmul(Ainv, B)
print(X)