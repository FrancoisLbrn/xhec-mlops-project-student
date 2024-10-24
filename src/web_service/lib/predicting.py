import numpy as np
from sklearn.linear_model import Ridge


def predict(X: np.ndarray, model: Ridge) -> np.ndarray:
    """Make predictions using the model."""
    return model.predict(X)
