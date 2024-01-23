from sympy import symbols, factorial
from B1 import B1

u = symbols('u')



def bb1eval(c, du, u):
    # Initialize the sum of evaluated terms
    fx = 0
    fy = 0

    # Loop over control points
    for j in range(du + 1):
        fx += c[j][0] * B1(j, du, u)
        fy += c[j][1] * B1(j, du, u)

    return fx,fy

# Example usage
test = 1
if test == 1:
    du = 2
    u = 0.5
    # Example control point matrix, replace with the actual data
    control_points = [[1, 2], [0, 2], [0, 1]]
    

    result = bb1eval(control_points, du, u)
    print(result)
