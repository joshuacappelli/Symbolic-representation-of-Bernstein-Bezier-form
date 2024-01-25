from sympy import symbols, factorial
from B1 import B1

u = symbols('u')



def bb1eval(c, du, u):
    # Initialize the sum of evaluated terms
    f = 0

    # Loop over control points
    for j in range(du + 1):
        f += c[j] * B1(j, du, u)

    return f

# Example usage
test = 1
if test == 1:
    du = 2
    u = 0.5
    # Example control point matrix, replace with the actual data
    control_points = [1,0,1]
    

    result = bb1eval(control_points, du, u)
    print(result)
