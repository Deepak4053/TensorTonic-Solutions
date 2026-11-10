import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    y_pred = np.clip(y_pred, 1e-15, 1.0)
    n = len(y_true)
    correct_probs = y_pred[np.arange(n), y_true]
    loss = -np.mean(np.log(correct_probs))
    
    return float(loss)
    