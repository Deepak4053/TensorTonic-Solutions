import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    _,classes = np.unique(y,return_counts = True)
    pi = classes /len(y)
    entropy = -np.sum(pi * np.log2(pi + 1e-9))
    return max(0.0 , entropy)
    
    