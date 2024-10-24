import argparse
from pathlib import Path

import pandas as pd
from config import DATA_DIRPATH, LOCAL_OBJECTS_DIRPATH
from prefect import flow
from preprocessing import preprocess_data
from training import train_model
from utils import save_pickle


@flow(name="train-model")
def main(trainset_path: Path = DATA_DIRPATH) -> None:
    """
    Train a machine learning model using the dataset located at the specified path,
    and save both the trained model and the data preprocessor as pickle files.

    Parameters:
        trainset_path (Path): The file path to the training dataset directory.
        Defaults to DATA_DIRPATH.

    Steps:
    1. Loads the dataset from the provided directory.
    2. Preprocesses the data, including features and target variable extraction.
    3. Saves the preprocessor object for future data transformations.
    4. Trains the machine learning model using the preprocessed features and labels.
    5. Saves the trained model as a pickle file for future use.

    Returns:
        None
    """

    # 1.Read data
    df = pd.read_csv(f"{trainset_path}/abalone.csv")

    # 2.Preprocess data
    x, y, preprocessor = preprocess_data(
        df,
        is_train=True,
        with_target=True,
    )

    # 3. Pickle data encoder
    save_pickle(f"{LOCAL_OBJECTS_DIRPATH}/preprocessor.pkl", preprocessor)

    # 4. Train model
    model = train_model(x, y)

    # 5. Pickle model
    save_pickle(f"{LOCAL_OBJECTS_DIRPATH}/model.pkl", model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model using the data at the given path."
    )
    parser.add_argument(
        "trainset_path",
        type=str,
        nargs="?",
        default=DATA_DIRPATH,
        help="Path to the training set",
    )
    args = parser.parse_args()
    main(args.trainset_path)
