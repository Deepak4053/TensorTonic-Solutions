import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    predictions = np.array(predictions)
    result = []
    for col in predictions.T:
        values, counts = np.unique(col, return_counts=True)
        result.append(values[np.argmax(counts)])

    return result