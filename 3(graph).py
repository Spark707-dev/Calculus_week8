import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**3 - 5*x**2 + 30

# Define the range of x values (from 0 to 4)
x = np.linspace(0, 4, 400)
y = f(x)

# Plot the graph
plt.plot(x, y, label=r'$f(x) = x^3 - 5x^2 + 30$')
plt.title('Graph of f(x) = x^3 - 5x^2 + 30')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
