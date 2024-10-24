import argparse
from pathlib import Path

import pandas as pd
from config import DATA_DIRPATH, LOCAL_OBJECTS_DIRPATH
from preprocessing import preprocess_data
from training import train_model
from utils import save_pickle


def main(trainset_path: Path = DATA_DIRPATH) -> None:
    """
    Train a model using the data at the given path and save the model (pickle).
    """
    # Read data
    df = pd.read_csv(f"{DATA_DIRPATH}/abalone.csv")
    # Preprocess data
    x, y, preprocessor = preprocess_data(
        df,
        is_train=True,
        with_target=True,
    )

    # Pickle data encoder
    save_pickle(f"{LOCAL_OBJECTS_DIRPATH}/preprocessor.pkl", preprocessor)

    # Train model
    model = train_model(x, y)

    # Pickle model
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
