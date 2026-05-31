def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    if not ground_truth :
        return 0.0
    hits = 0
    for recom , truth in zip(recommendations,ground_truth):
        if any(item in recom[:k] for item in truth):
            hits +=1
            
    return hits/len(ground_truth)       