import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    res =[]
    for i in range(len(k)):
        temp =k[i]
        ans = 1
        for j in range(1,temp):
            ans = ans*(1-p)
        pmf =ans*p
        res.append(pmf)
    mean = 1/p
    mean =float(mean)
    res =np.array(res)
    return (res ,mean)
    