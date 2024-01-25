import numpy as np
import matplotlib.pyplot as plt
from bb1eval import bb1eval

def bezier_curve(control_points, num_points=100):
    """
    Generate points for a cubic Bézier curve.

    Parameters:
    - control_points (list of lists): Control points of the Bézier curve.
    - num_points (int): Number of points to generate on the curve.

    Returns:
    - np.ndarray: Array containing points on the Bézier curve.
    """
    n = len(control_points) - 1 # degree

    t_values = np.linspace(0, 1, num_points)
    curve_points = np.zeros((num_points, len(control_points[0])))
    print(curve_points)

    for i, t in enumerate(t_values):
        for j in range(n + 1):
            
            curve_points[i] += control_points[j] * np.math.comb(n, j) * ((1 - t) ** (n - j)) * (t ** j)
            #curve_points[i] += bb1eval(control_points[j],i,t)

    print(curve_points)

    return curve_points

def plot_bezier_curve(control_points):
    """
    Plot a cubic Bézier curve.

    Parameters:
    - control_points (list of lists): Control points of the Bézier curve.
    """
    curve_points = bezier_curve(control_points)

    plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
    plt.plot(curve_points[:, 0], curve_points[:, 1], label='Bézier Curve')
    
    plt.title('Cubic Bézier Curve')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example: Plotting a Bézier curve with control points
control_points = np.array([[0, 0], [1, 2], [3, 1], [4, 3]])
plot_bezier_curve(control_points)
