import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A =np.array(A)
    n = len(A)
    m = len(A[0])
    sm = 0
    for i in range(n):
        for j in range(m):
            if i == j:
                sm +=A[i][j]
    return sm            
