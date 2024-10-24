import pickle


def load_pickle(path: str):
    """Load an object from a pickle file."""

    with open(path, "rb") as f:
        loaded_obj = pickle.load(f)
    return loaded_obj
