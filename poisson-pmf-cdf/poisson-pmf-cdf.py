import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    
    kfact = 1
    for i in range(1,k+1):
        kfact = kfact *i

    pmf = (np.exp(-lam) * (lam ** k)) / kfact
    cdf = 0
    for i in range(0, k + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        cdf += (np.exp(-lam) * (lam ** i)) / fact

    return (pmf, cdf)
