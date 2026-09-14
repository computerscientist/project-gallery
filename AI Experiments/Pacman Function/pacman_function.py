import numpy as np
import matplotlib.pyplot as plt

alpha = np.pi / 6
tan_alpha = np.tan(alpha)

x = np.linspace(-1.2, 1.2, 1000)
y = np.linspace(-1.2, 1.2, 1000)
X, Y = np.meshgrid(x, y)

circle_term = X**2 + Y**2 - 1
mouth_term = tan_alpha * X - np.abs(Y)

F = np.maximum(circle_term, mouth_term)

fig, ax = plt.subplots(figsize=(6, 6))

ax.contour(
    X,
    Y,
    F,
    levels=[0]
)

ax.set_aspect("equal")
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()