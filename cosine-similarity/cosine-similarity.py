import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    dot = np.dot(a,b)
    mod1 =np.linalg.norm(a)
    mod2 = np.linalg.norm(b)

    if mod1 == 0 or mod2 ==0:
        return 0.0
    return dot/(mod1*mod2)    