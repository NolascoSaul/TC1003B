import sympy as sp
import math

sqrt = math.sqrt

A = sp.Matrix([
    [1, 2, 0],
    [0, 3, 0],
    [2, -4, 2]
])

lam = sp.Symbol('lambda')
M = sp.Matrix([
    [1-lam, 2, 0],
    [0, 3-lam, 0],
    [2, -4, 2-lam]
])

PC = M.det()

#print(sp.solve(PC, lam))

MA = sp.Matrix([
    [0, 2, 0, 0],
    [0, 2, 0, 0],
    [2, -4, 1, 0],
])
# print(MA.rref())

MM = sp.Matrix([
    [-1, 2, 0, 0],
    [0, 1, 0, 0],
    [2, -4, 0, 0],
])

