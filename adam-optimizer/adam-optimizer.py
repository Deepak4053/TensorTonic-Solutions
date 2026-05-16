import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    param = np.array(param, dtype=float)
    grad  = np.array(grad, dtype=float)
    m = np.array(m, dtype=float)
    v = np.array(v, dtype=float)

    mt = beta1*m + (1-beta1)*grad
    vt = beta2 *v + (1- beta2)*grad**2
    mt_hat = mt /(1-beta1**t)
    vt_hat = vt /(1-beta2**t)

    param_new = param - lr *mt_hat/(np.sqrt(vt_hat) + eps)

    return param_new ,mt ,vt
        
    