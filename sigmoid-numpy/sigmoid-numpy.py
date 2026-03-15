import numpy as np

def sigmoid(x):
    x = np.asarray(x, dtype=float)
    sigma=1 / (1 + np.exp(-x))
    return sigma