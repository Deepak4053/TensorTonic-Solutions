import numpy as np
def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    data = np.array(data)
    minm =np.min(data,axis =0)
    maxm = np.max(data , axis =0)
    diff = maxm - minm
    diff[diff == 0] = 1

    scalled = (data -minm)/diff
    
    return scalled.tolist()