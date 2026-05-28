import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    w=np.array(w)
    g =np.array(g)
    G = np.array(G)
    
    Gt = G + g**2
    Wt = w - (lr/(np.sqrt(Gt+eps)))*g
    return (Wt,Gt)