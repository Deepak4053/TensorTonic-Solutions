import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    tp = np.sum(y_pred == y_true)
    fp = np.sum(y_pred != y_true)
    fn = fp

    f1 = 2*tp/(2*tp + fp + fn)
    return f1
    
            
    
    
    
        