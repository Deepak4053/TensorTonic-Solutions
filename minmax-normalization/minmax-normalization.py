import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """

    X = np.array(X, dtype=float)
    if X.ndim == 2:
        if axis == 0:
            minm = np.min(X, axis=0)
            maxm = np.max(X, axis=0)
        else:
            minm = np.min(X, axis=1, keepdims=True)
            maxm = np.max(X, axis=1, keepdims=True)
        ans = (X - minm) / (maxm - minm + eps)

    else:
        minm = np.min(X)
        maxm = np.max(X)
        ans = (X - minm) / (maxm - minm + eps)

    return ans