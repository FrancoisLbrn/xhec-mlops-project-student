import numpy as np
from sklearn.linear_model import Ridge


def predict(X: np.ndarray, model: Ridge) -> np.ndarray:
    """
    Make predictions on input data using a pre-trained Ridge regression model.

    Parameters:
        X (np.ndarray): A 2D NumPy array of input features where each row represents
                        a data sample and each column represents a feature.
        model (Ridge): A pre-trained Ridge regression model used to make predictions.

    Returns:
        np.ndarray: A 1D NumPy array of predicted values corresponding
        to the input data.
    """

    return model.predict(X)
