from sympy.tensor.array.expressions import ArraySymbol
import sympy
from sympy import symbols

def bb1add(dg, b1, b2, b1_cof, b2_cof):
    # the length of multipliers
    b1_summands = len(b1_cof)
    b2_summands = len(b2_cof)

    # Because of the property of ArraySymbol, we need to store the element of ArraySymbol into list to do the computation
    b1_local = b1
    b2_local = b2

    print(b1_local)
    print(b2_local)
    # The algorithm
    out = [0] * (dg + 1)
    print("this is the out: ")
    print(out)
    for i in range(dg + 1):
        # Computate b1
        for j in range(b1_summands):
            out[i] += b1_local[i] * b1_cof[j]
        # Computate b2
        for k in range(b2_summands):
            out[i] += b2_local[i] * b2_cof[k]

    return out

dg = 1  # the degree of b1 and b2

b1 = [sympy.symbols('b1_%d' % i) for i in range(dg+1)]
b2 = [sympy.symbols('b2_%d' % i) for i in range(dg+1)]
# Manual input of multipliers
b1_cof = [-1]
b2_cof = [2,3,5]

bb = bb1add(dg, b1, b2, b1_cof, b2_cof)
print(bb)
