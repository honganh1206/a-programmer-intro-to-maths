import math

import matplotlib.pyplot as plt


def bezier(t, points):
    n = len(points) - 1

    x = 0
    y = 0

    for i in range(n + 1):
        coeff = math.comb(n, i) * (1 - t) ** (n - i) * t ** i
        x += coeff * points[i][0] # x value of Pi
        y += coeff * points[i][1] # y value of Pi

    return x, y

def bezier_derivative(t, points):
    n = len(points) - 1

    if n == 0:
        return (0.0, 0.0)

    dx = 0
    dy = 0

    for i in range(n):
        coeff = n * math.comb(n - 1, i) * (1 - t) ** (n - 1 - i) * t ** i
        dx += coeff * (points[i + 1][0] - points[i][0])
        dy += coeff * (points[i + 1][1] - points[i][1])

    return dx, dy


#
# points = [
#     (0, 0),
#     (1, 3),
#     (3, 3),
#     (4, 0)
# ]
#
# # Evaluate B(t) at 101 different values
# t_values = [i / 100 for i in range(101)]
# curve = [bezier(t, points) for t in t_values]
#
# # Separate x and y coordinates
# x_values = [p[0] for p in curve]
# y_values = [p[1] for p in curve]
#
# control_x = [p[0] for p in points]
# control_y = [p[1] for p in points]
#
# # Plot the Bézier curve
# plt.plot(x_values, y_values, label="Bézier curve")
#
# # Plot the control polygon
# plt.plot(
#     control_x,
#     control_y,
#     "o--",
#     label="Control points"
# )
#
# plt.axis("equal")
# plt.grid(True)
# plt.legend()
# plt.show()
