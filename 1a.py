from scipy.integrate import quad
import numpy as np

def f(x):
    return 3 * np.sqrt(x)

result, _ = quad(f, 4, 9)

print("Definite integral value:", result)
