import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g = np.array(g)
    modg =np.linalg.norm(g)
    if modg == 0 or max_norm <= 0:
        return g
    if modg > max_norm :
        return g*(max_norm/modg)
    else:
        return g