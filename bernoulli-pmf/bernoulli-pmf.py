import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    res = []
    for num in x :
        if num==1:
            pmf =p
        else:
            pmf =1-p
        res.append(pmf)   
    res =np.array(res)   
    mean = p
    var = float(p*(1-p))
    return  (res ,mean ,var )