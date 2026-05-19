import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x)
    p = np.array(p)
    total_p =np.sum(p)
    
    if len(x) != len(p):
        raise ValueError
    if not np.allclose(np.sum(p), 1):
        raise ValueError
    else:
        Expected_val =np.sum(x*p)
    return Expected_val