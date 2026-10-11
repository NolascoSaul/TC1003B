import numpy as np
import matplotlib.pyplot as plt

mat = np.array([
    [1, 1, 1, 6],
    [2, 0, -1, 4],
    [0, 0, 3, 3],
    [1, 0, 0, 5]
])

det = np.linalg.det(mat)

print(det)