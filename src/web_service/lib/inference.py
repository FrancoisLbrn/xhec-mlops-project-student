from typing import List

import numpy as np
import pandas as pd
from loguru import logger
from sklearn.base import BaseEstimator
from sklearn.compose import ColumnTransformer

from models import InputData
from ..modelling.preprocessing import compute_target, fit_preprocessor, extract_x_y, preprocess_data


def run_inference(input_data: List[InputData], preprocessor: ColumnTransformer, model: BaseEstimator) -> np.ndarray:
    """Run inference on a list of input data.

    Args:
        input_data: the data points to run inference on.
        preprocessor (ColumnTransformer): the fitted ColumnTransformer object.
        model (BaseEstimator): the fitted model object.

    Returns:
        np.ndarray: the predicted abalone ages in years.
    """
    logger.info(f"Running inference on:\n{input_data}")
    df = pd.DataFrame([x.dict() for x in input_data])
    x, _, _ = preprocess_data(df, is_train=False, preprocessor=preprocessor, with_target=False)
    y = predict(x, model)
    logger.info(f"Predicted trip durations:\n{y}")
    return y
