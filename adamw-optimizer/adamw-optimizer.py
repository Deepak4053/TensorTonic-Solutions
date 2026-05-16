import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    
    w = np.array(w)
    grad  = np.array(grad)
    m = np.array(m)
    v = np.array(v)

    mt = beta1*m + (1-beta1)*grad
    vt = beta2 *v + (1- beta2)*grad**2

    w_new = w -lr *(weight_decay*w) - lr *mt/(np.sqrt(vt)+eps)

    return  (w_new ,mt,vt)

    