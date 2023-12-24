from sympy import symbols, factorial
from B1 import B1

u = symbols('u')



def bb1eval(c, du, u):
    # Initialize the sum of evaluated terms
    f = 0

    # Loop over control points
    for j in range(du + 1):
        # Evaluate the term and add it to the sum
        # print("B1: " , B1(j, du, u))
        # print("control points: " , c[j])
        
        f += c[j][du - j] * B1(j, du, u)

    return f

# Example usage
test = 0
if test == 1:
    du = 2
    u = 0.5
    # Example control point matrix, replace with the actual data
    control_points = [[1, 2, 1], [0, 1, 0], [0, 0, 1]]

    result = bb1eval(control_points, du, u)
    print(result)
