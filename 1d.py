import numpy as np
from scipy.integrate import quad

# Define the integrand
def integrand(x):
    return np.pi * np.cos(np.pi * x / 2)

# Compute the definite integral from -1 to 1
result, error = quad(integrand, -1, 1)

print("Integral result:", result)
print("Estimated error:", error)
