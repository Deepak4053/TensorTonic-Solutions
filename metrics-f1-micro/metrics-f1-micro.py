import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    TP =0
    FP =0
    FN =0
    for i,j in zip(y_true,y_pred):
        if i == j :
            TP +=1
        else:
            FP +=1
    FN = FP    
    f1 = 2*TP/(2*TP + FP + FN)  
    return f1
            
    
    
    
        