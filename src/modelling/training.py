import numpy as np
from sklearn.linear_model import Ridge


def train_model(X: np.ndarray, y: np.ndarray) -> Ridge:
    """Fit a Ridge model on the data."""
    model = Ridge(alpha=1.0, fit_intercept=False)
    model.fit(X, y)
    return model
