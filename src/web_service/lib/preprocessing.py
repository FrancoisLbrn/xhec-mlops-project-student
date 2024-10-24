from typing import List, Tuple

import numpy as np
import pandas as pd
from lib.config import CATEGORICAL_COLS, NUMERICAL_COLS
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def fix_column_names(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        df[col] = df[col].str.replace(" ", "_")
    return df


def compute_target(
    df: pd.DataFrame, rings_column: str = "Rings"
) -> pd.DataFrame:
    """Compute the abalone age based on the number of rings."""

    df["Age"] = df[rings_column] + 1.5
    return df


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


def extract_x_y(
    df: pd.DataFrame,
    preprocessor: ColumnTransformer = None,
    with_target: bool = True,
) -> Tuple[np.ndarray, np.ndarray, ColumnTransformer]:
    """Extract X and y from the dataframe."""

    y = None
    if with_target:
        y = df["Age"].values
    x = preprocessor.transform(df)
    return x, y


def preprocess_data(
    df: pd.DataFrame,
    is_train: bool = True,
    preprocessor: ColumnTransformer = None,
    with_target: bool = True,
) -> Tuple[np.ndarray, np.ndarray, ColumnTransformer]:
    """Preprocess the data and return X, y, and the preprocessor."""

    df = fix_column_names(df)
    df = compute_target(df)
    if is_train:
        preprocessor = fit_preprocessor(df)
    x, y = extract_x_y(
        df=df, preprocessor=preprocessor, with_target=with_target
    )
    return x, y, preprocessor
