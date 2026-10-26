"""Plot max(x**2 + y**2, 1 + tan(alpha)*x - abs(y)) = 1."""

import numpy as np
import matplotlib.pyplot as plt

# Half the mouth-opening angle, in radians: 0 < alpha < pi/2.
alpha = np.pi / 6
# Use alpha = np.pi / 4 for max(x**2 + y**2, 1 + x - abs(y)) = 1.

x = np.linspace(-1.2, 1.2, 1000)
y = np.linspace(-1.2, 1.2, 1000)
X, Y = np.meshgrid(x, y)

# Evaluate the left-hand side of the equation directly.
# np.tan(alpha) * X means (tan alpha) times X, not tan(alpha * X).
F = np.maximum(X**2 + Y**2, 1 + np.tan(alpha) * X - np.abs(Y))

fig, ax = plt.subplots(figsize=(6, 6))

# The outline is F = 1. The filled Pac-Man domain would be F <= 1.
ax.contour(X, Y, F, levels=[1])

ax.set_aspect("equal")
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"$\max(x^2+y^2,\ 1+(\tan\alpha)x-|y|)=1$")

plt.show()
