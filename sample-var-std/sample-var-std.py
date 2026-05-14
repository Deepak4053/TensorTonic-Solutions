import numpy as np
def sample_var_std(x):
    n = len(x)
    div = 1/(n-1)
    sm = 0
    mean = np.mean(x)
    for i in range(n):
        temp = x[i] - mean
        sm += temp*temp
    var =div*sm
    std = np.sqrt(var)
    return var,std  
  




    