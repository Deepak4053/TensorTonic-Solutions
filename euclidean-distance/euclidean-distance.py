import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    if len(x)!= len(y):
        raise ValueError
    dist = 0
    for i in range(len(x)):
        dist +=(x[i]-y[i])**2
    dist =np.sqrt(dist)   
    return dist