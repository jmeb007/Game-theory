import sympy as sy
from sympy.solvers import solve
from sympy import evaluate
import numpy as np
# escribir las columnas
b1 = [10, 3, 5, 9]
b2 = [3, 5, 4, 3]
b3 = [0, 8, 5, 0]
b4 = [2, 10, 5, -10]
print(" ")
# determinar si son dominadas
if b1[1] or b1[2] or b1[3] > b1[0]:
    print("a1_1 si")
if b2[1] or b1[2] or b2[3] > b2[0]:
    print("a1_2 si")
if b3[1] or b3[2] or b3[3] > b3[0]:
    print("a1_3 si")
if b4[1] or b4[2] or b4[3] > b4[0]:
    print("a1_4 si")
if b1[1]+b1[2]+b1[3] > b1[0] and b2[1]+b1[2]+b2[3] > b2[0] and b3[1]+b3[2]+b3[3] > b3[0] and b4[1]+b4[2]+b4[3] > b4[0]:
    print("a1 se encuentra dominada")
print(" ")
# a2
if b1[0] or b1[2] or b1[3] > b1[1]:
    print("a2_1 si")
if b2[0] or b2[2] or b2[3] > b2[1]:
    print("a2_2 si")
if b3[0] or b3[2] or b3[3] > b3[1]:
    print("a2_3 si")
if b4[0] or b4[2]or b4[3] > b4[1]:
    print("a2_4 si")
if b1[0] or b1[2]+b1[3] > b1[1] and b2[0]+b2[2]+b2[3] > b2[1] and b3[0]+b3[2]+b3[3] > b3[1] and  b4[0]+b4[2]+b4[3] > b4[1]:
    print(" a2 se encuentra dominada")
print(" ")
# a3
if b1[0] or b1[1] or b1[3] > b1[2]:
    print("a3_1 si")
if b2[0] or b2[1] or b2[3] > b2[2]:
    print("a3_2 si")
if b3[0] or b3[1] or b3[3] > b3[2]:
    print("a3_3 si")
if b4[0] or b4[1] or b4[3] > b4[2]:
    print("a3_4 si")
if b1[0]+b1[1]+b1[3] > b1[2] and b2[0]+b2[1]+b2[3] > b2[2] and b3[0]+b3[1]+b3[3] > b3[2] and b4[0]+b4[1]+b4[3] > b4[2]:
    print(" a3 se encuentra dominada")
print("")
# a3
if b1[0] or b1[1] or b1[2] > b1[3]:
    print("a4_1 si")
if b2[0] or b2[1] or b2[2] > b2[3]:
    print("a4_2 si")
if b3[0] or b3[1] or b3[2] > b3[3]:
    print("a4_3 si")
if b4[0] or b4[1] or b4[2] > b4[2]:
    print("a4_4 si")
if b1[0] or b1[1]+b1[2] > b1[3] and b2[0]+b2[1]+b2[2] > b2[3] and b3[0]+b3[1]+b3[2] > b3[3] and b4[0]+b4[1]+b4[2] > b4[2]:
    print("a4 se encuentra dominada")