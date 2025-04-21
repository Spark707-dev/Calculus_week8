from scipy.integrate import quad
import numpy as np

# Define the function
def f(x):
    return 3 * np.sqrt(x)

# Compute the definite integral from 4 to 9
result, _ = quad(f, 4, 9)

print("Definite integral value:", result)
