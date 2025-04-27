import numpy as np
from scipy.integrate import quad

def integrand(x):
    return np.arccos(x)

result, error = quad(integrand, 0, 1)

print("Integral result:", result)
print("Estimated error:", error)
