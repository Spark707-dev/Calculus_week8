import numpy as np
from scipy.integrate import quad

def f(x):
    return x**3 - 5*x**2 + 30

integral, error = quad(f, 0, 4)

average_value = integral / (4 - 0)

print(f"The average value of the function over [0, 4] is: {average_value}")
