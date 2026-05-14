import numpy as np
def sample_var_std(x):
    x = np.array(x)
    mean = np.mean(x)
    var = np.sum((x - mean)**2) / (len(x) - 1)
    std = np.sqrt(var)
    return var, std  
  




    