import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    res =[]
    for num in x :
        if num >= 0:
            temp = num
        else:
            temp =alpha * num
        res.append(temp)
    res = np.array(res)  
    return res
    