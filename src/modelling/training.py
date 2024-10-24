import numpy as np
from sklearn.linear_model import Ridge


def train_model(X: np.ndarray, y: np.ndarray) -> Ridge:
    """Train a Ridge model on the data."""
    model = Ridge()
    model.fit(X, y)
    return model
