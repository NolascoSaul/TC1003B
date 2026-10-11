import numpy as np 

alfabeto = 'zyxwvutsrqpoñnmlkjihgfedcba'
alfabeto = list(alfabeto)

A = np.array([
    [1, 2, -3, 4, 5],
    [-2, -5, 8, -8, -9],
    [1, 2, -2, 7, 9],
    [1, 1, 0, 6, 12],
    [2, 4, -6, 8, 11]
])

Ainv = np.linalg.inv(A)

msg = np.array([
    [68,116,-123,381,559],
    [98,161,-172,521,812],
    [34,21,25,208,410],
    [79,131,-157,375,587],
    [42,47,-32,214,382],
    [80,140,-176,384,559],
    [18,7,30,144,242],
    [23,32,-26,129,208]
])
    
X = np.matmul(msg, Ainv)

for i in range(len(X)):
    for j in range(len(X[0])):
        print(alfabeto[int(X[i][j])], end='')