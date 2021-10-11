import sympy as sy
from sympy.solvers import solve

min1 = [0]
max1 = [50]
min2 = [0]
max2 = [50]

s1 = sy.symbols("s1")
s2 = sy.symbols("s2")
# funcion 1 de utilidad y funcion 2
f1 = 100*s1-10*s1**2+10*s1*s2
f2 = 200*s2-15*s2**2+10*s1*s2

first_ds1 = sy.Derivative(f1, s1)
first_ds1 = first_ds1.doit()
first_ds2 = sy.Derivative(f2, s2)
first_ds2 = first_ds2.doit()
second_ds1 = sy.Derivative(f1, s1, s1)
second_ds1 = second_ds1.doit()
second_ds2 = sy.Derivative(f2, s2, s2)
second_ds2 = second_ds2.doit()
# a = f1+f2
# exp = sy.Derivative(a, s1)
# exp = exp.doit()
# print(solve(exp, s1))

print("primera derivada de funcion 1", first_ds1)
print("primera derivada de funcion 2", first_ds2)
if second_ds1 < 0:
    print("la funcion 1 es concava, proceder :3", second_ds1)

if second_ds2 < 0:
    print("la funcion 2 es concava", second_ds2)


a = solve(first_ds1, s1)
b = solve(first_ds2, s2)

print("r1=", a)
range1 = solve(a < min1)
range2 = solve(max1 < a)
print("range of the function 1", range1, range2)
print("actual range of the function 1", min1, max1)
print("r2=", b)
range3 = solve(b < min2)
range4 = solve(max2 < b)
print("range of the function 2", range3, range4)
print("actual range of the function 2", min2, max2)


nmat = ([first_ds1, first_ds2])
cons = ([s1, s2])

sist_eq = solve(nmat, cons)
print("punto de equilibrio de nash", sist_eq)
