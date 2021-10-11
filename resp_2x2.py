import sympy as sy
from sympy.solvers import solve
from sympy import evaluate
import numpy as np

# valores del jugador 1
j1 = sy.Array([3, 9, 4, 6])
# valores del jugador 2
j2 = [3, 2, 5, 7]
x = sy.symbols("x")
y = sy.symbols("y")

u1 = j1[0]*x*y+j1[1]*x*(1-y)+j1[2]*(1-x)*y+j1[3]*(1-x)*(1-y)
u2 = j2[0]*x*y+j2[1]*x*(1-y)+j2[2]*(1-x)*y+j2[3]*(1-x)*(1-y)

print("u1 simplificada", sy.simplify(u1))
print("u2 simplificada", sy.simplify(u2))

first_ds1 = sy.Derivative(u1, x)
first_ds1 = first_ds1.doit()
first_ds2 = sy.Derivative(u2, y)
first_ds2 = first_ds2.doit()
print("la primera derivada de u1 por dx:", first_ds1)
print("la primera derivada de u2 por dy:", first_ds2)
a = solve(first_ds1)
b = solve(first_ds2)

print("el maximo para u1 es:", a)
print("el maximo para u2 es:", b)

