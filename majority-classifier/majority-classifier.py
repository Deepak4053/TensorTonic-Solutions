import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples using NumPy.
    """
    labels, counts = np.unique(y_train, return_counts=True)
    majority = np.argmax(counts)
    majority_label = labels[majority]
    
    ans = np.full(shape=len(X_test), fill_value=majority_label)
    return ans
