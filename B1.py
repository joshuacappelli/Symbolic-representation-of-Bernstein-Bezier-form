# Univariate parameter B
from sympy import symbols, factorial

u = symbols('u')

# univariate Parameter B
def B1(i, dg, u):
    
    # ith univariate BB form of degree dg
    j = dg - i
    b = (factorial(dg) / (factorial(j) * factorial(i))) * (1 - u)**j * u**i
    return b

#-----------------
test = 0  # Set test to 1 to execute the code inside the if statement
if test == 1:
    h = B1(1, 2, u)
    print(h)

