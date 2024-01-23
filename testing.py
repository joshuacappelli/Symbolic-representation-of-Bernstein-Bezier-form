import matplotlib.pyplot as plt
import numpy as np
from bb1eval import bb1eval

def plot_bezier_curves(control_points, degrees, num_points=100):
    # Generate a list of 'u' values from 0 to 1
    u_values = np.linspace(0, 1, num_points)

    # Initialize lists to store x and y coordinates of the curves
    curves_x = []
    curves_y = []

    # Evaluate the Bezier curves for each 'u' value and each degree
    for degree in degrees:
        curve_x = []
        curve_y = []
        for u in u_values:
            result = bb1eval(control_points, degree, u)
            curve_x.append(result[0])
            curve_y.append(result[1])
        curves_x.append(curve_x)
        curves_y.append(curve_y)

    # Plot the Bezier curves
    for i, degree in enumerate(degrees):
        plt.plot(curves_x[i], curves_y[i], label=f'Degree {degree}')

    # Plot control points and annotate them with coordinates
    colors = ['red', 'green', 'blue', 'purple', 'orange']
    for i, point in enumerate(control_points):
        plt.scatter(point[0], point[1], color=colors[i], label=f'Point {i + 1}')
        plt.annotate(f'({point[0]}, {point[1]})', (point[0], point[1] + 0.1))

    plt.title('Bezier Curves with Control Points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()

# Example usage
test = 1
if test == 1:
    # Example control point matrix, replace with the actual data
    control_points = [[-2, 2], [3, 5], [1, 6], [4, 4]]

    # Plot Bezier curves of different degrees
    degrees = [1, 2, 3]  # Add more degrees as needed

    plot_bezier_curves(control_points, degrees)
