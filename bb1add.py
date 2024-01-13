from sympy.tensor.array.expressions import ArraySymbol
import sympy
from sympy import symbols

def bb1add(dg, b1, b2, b1_cof, b2_cof):
    # The algorithm
    out = [0] * (dg + 1)
    for i in range(dg + 1):
        # Computate b1
        for j in range(len(b1_cof)):
            out[i] += b1[i] * b1_cof[j]
        # Computate b2
        for k in range(len(b2_cof)):
            out[i] += b2[i] * b2_cof[k]

    return out


test = 0
if test == 1:
    dg = 1  # the degree of b1 and b2

    b1 = [sympy.symbols('b1_%d' % i) for i in range(dg+1)]
    b2 = [sympy.symbols('b2_%d' % i) for i in range(dg+1)]
    # Manual input of multipliers
    b1_cof = [-1]
    b2_cof = [2,3,5]

    bb = bb1add(dg, b1, b2, b1_cof, b2_cof)
    print(bb)
