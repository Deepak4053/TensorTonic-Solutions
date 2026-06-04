import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.array(x)
    sigma_X = 1/(1+ np.exp(-x))
    swish_act = sigma_X * x
    return swish_act