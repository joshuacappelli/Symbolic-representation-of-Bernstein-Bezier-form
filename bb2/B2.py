from sympy import symbols, factorial

# Define symbols
x, y = symbols('x y')

def B2(i, j, dg, u, v):
    w = 1 - u - v
    k = dg - i - j
    out = factorial(dg) / (factorial(i) * factorial(j) * factorial(k)) * (u**i) * (v**j) * (w**k)
    return out

# Test cases
test = 1

if test == 1:
    bb = B2(1, 1, 3, x, y)
    print(bb)
    print("should be 6*x*y*(1-x-y)")

if test == 2:
    bb = B2(1, 1, 3, 1/3, 1/3)
    print(bb)
    print("should be 6/27")
