import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v = np.array(v)
    n = len(v)
    mat =np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i == j:
                mat[i][j]=v[i]
    return mat           
