import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    if len(x)!=len(y):
        raise ValueError
    ans = 0
    for i in range(len(x)):
        ans +=x[i]*y[i]
    return ans    