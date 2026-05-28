import numpy as np

def stratified_split(X, y, test_size=0.2, rng=None):
    rng = np.random.default_rng(rng)
    X = np.array(X)
    y = np.array(y)
    train_idx = []
    test_idx = []
    classes = np.unique(y)
    for cls in classes:
        cls_idx = np.where(y == cls)[0]
        rng.shuffle(cls_idx)
        n_test = round(len(cls_idx) * test_size)
        test_idx.extend(cls_idx[:n_test])
        train_idx.extend(cls_idx[n_test:])
    train_idx = np.array(sorted(train_idx), dtype=int)
    test_idx = np.array(sorted(test_idx), dtype=int)

    return (
        X[train_idx],
        X[test_idx],
        y[train_idx],
        y[test_idx]
    )