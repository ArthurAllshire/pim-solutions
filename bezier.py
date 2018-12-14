import matplotlib.pyplot as plt
import numpy as np

points = [[0, 0], [1, 1], [0, 1]]


def quadratic_bezier(t, p0, p1, p2):
    B_t = (1-t)*((1-t)*p0 + t*p1) + t*((1-t)*p1 + t*p2)
    return B_t


plt.figure()
plt.title("Quadratic Bezier")
plt.xlabel("$x$-Axis")
plt.ylabel("$y$-Axis")
x = []
y = []
T = np.linspace(0, 1, 100)
for t in T:
    x.append(quadratic_bezier(t, points[0][0], points[1][0], points[2][0]))
    y.append(quadratic_bezier(t, points[0][1], points[1][1], points[2][1]))
bezier, = plt.plot(x, y, 'C3', label="Bezier Curve")
control = plt.scatter([points[0][0], points[1][0], points[2][0]],
                      [points[0][1], points[1][1], points[2][1]],
                      label="Control Points")
plt.legend(handles=[bezier, control])
plt.savefig("bezier.png")
