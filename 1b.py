from scipy.integrate import quad
import numpy as np

def f(x):
    return np.log(x)

result, _ = quad(f, 1, np.e)

print("Result:", round(result, 4))