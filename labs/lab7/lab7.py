import numpy as np
import matplotlib.pyplot as plt


def Y(x):
    return x ** np.sin(10 * x)

x = np.linspace(1, 10, 1000)

y = Y(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r"$Y(x) = x^{\sin(10x)}$", color="blue")

plt.title("Графік функції $Y(x) = x^{\sin(10x)}$", fontsize=14)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$Y(x)$", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.show()

