import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """

    nl = len(y_left)
    nr = len(y_right)
    N = nl + nr

    if N == 0:
        return 0.0

    if nl == 0:
        gini_l = 0.0
    else:
        _, l_counts = np.unique(y_left, return_counts=True)
        p_left = l_counts / nl
        gini_l = 1 - np.sum(p_left ** 2)

    if nr == 0:
        gini_r = 0.0
    else:
        _, r_counts = np.unique(y_right, return_counts=True)
        p_right = r_counts / nr
        gini_r = 1 - np.sum(p_right ** 2)

    return (nl / N) * gini_l + (nr / N) * gini_r