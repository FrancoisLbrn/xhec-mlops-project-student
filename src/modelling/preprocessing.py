from typing import List, Tuple

import numpy as np
import pandas as pd
from config import CATEGORICAL_COLS, NUMERICAL_COLS
from prefect import flow, task
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


@task
def fix_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Replace spaces in column names with underscores."""
    columns = df.columns
    columns_fixed = [col.replace(" ", "_") for col in columns]
    df.columns = columns_fixed
    return df


@task
def compute_target(
    df: pd.DataFrame, rings_column: str = "Rings"
) -> pd.DataFrame:
    """Compute the abalone age based on the number of rings."""

    df["Age"] = df[rings_column] + 1.5
    return df


@task
def fit_preprocessor(
    df: pd.DataFrame,
    numerical_features: List[str] = None,
    categorical_features: List[str] = None,
) -> Pipeline:
    """Fit the adapted preprocessor to the data."""

    if numerical_features is None:
        numerical_features = NUMERICAL_COLS
    numerical_transformer = Pipeline(steps=[("scaler", StandardScaler())])
    if categorical_features is None:
        categorical_features = CATEGORICAL_COLS
    categorical_transformer = Pipeline(
        steps=[("onehot", OneHotEncoder(handle_unknown="ignore"))]
    )
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numerical_transformer, numerical_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )
    preprocessor.fit(df)
    return preprocessor


@task
def extract_x_y(
    df: pd.DataFrame,
    preprocessor: ColumnTransformer = None,
    with_target: bool = True,
) -> Tuple[np.ndarray, np.ndarray, ColumnTransformer]:
    """Extract X and y from the dataframe.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing features and, optionally, the target variable.
    preprocessor : ColumnTransformer, optional
        A fitted ColumnTransformer object used to preprocess the features.
    with_target : bool, optional
        A flag indicating whether the dataset includes a target variable (y).

    Returns
    -------
    Tuple[np.ndarray, np.ndarray, ColumnTransformer]
        - x : np.ndarray
            Preprocessed feature matrix (X).
        - y : np.ndarray or None
            Target variable (y) as a numpy array if `with_target` is True;
            otherwise, None.
        - preprocessor : ColumnTransformer
            The ColumnTransformer used for preprocessing the features."""

    y = None
    if with_target:
        y = df["Age"].values
    x = preprocessor.transform(df)
    return x, y


@flow
def preprocess_data(
    df: pd.DataFrame,
    is_train: bool = True,
    preprocessor: ColumnTransformer = None,
    with_target: bool = True,
) -> Tuple[np.ndarray, np.ndarray, ColumnTransformer]:
    """Preprocess the data and return X, y, and the preprocessor.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing features and, optionally, the target variable.
    is_train : bool, optional
        Flag to indicate training mode or not. If True, the preprocessor
        will be fitted; otherwise, it will be applied to the data (default is True).
    preprocessor : ColumnTransformer, optional
        A ColumnTransformer to preprocess the features. If None and `is_train` is True,
        a new preprocessor will be fitted (default is None).
    with_target : bool, optional
        Flag indicating whether the target variable should be extracted.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray, ColumnTransformer]
        - x : np.ndarray
            Preprocessed feature matrix (X).
        - y : np.ndarray or None
            Target variable (y) as a numpy array if `with_target` is True;
            otherwise, None.
        - preprocessor : ColumnTransformer
            The fitted or used preprocessor for the features.
    """

    df = fix_column_names(df)
    if with_target:
        df = compute_target(df)
    if is_train:
        preprocessor = fit_preprocessor(df)
    x, y = extract_x_y(
        df=df, preprocessor=preprocessor, with_target=with_target
    )
    return x, y, preprocessor
