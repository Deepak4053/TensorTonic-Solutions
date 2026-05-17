def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    n = len(relevant)
    top_k = 0
    for i in range(k):
        if recommended[i] in relevant :
            top_k +=1
    Precision = top_k/k
    Recall = top_k /n

    return [Precision ,Recall]