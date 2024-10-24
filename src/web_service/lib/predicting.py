import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import root_mean_squared_error


def predict(X: np.ndarray, model: Ridge) -> np.ndarray:
    """Make predictions using the model."""
    return model.predict(X)


# To maybe remove
def evaluate_model(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Evaluate the model using the root mean squared error."""
    return root_mean_squared_error(y_true, y_pred)
