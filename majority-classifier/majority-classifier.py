from collections import Counter
import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    freq = Counter(y_train)
    most_common = freq.most_common()
    majority_label = most_common[0][0]
    ans = []
    for i in range(len(X_test)):
        ans.append(majority_label)
        
    return ans
