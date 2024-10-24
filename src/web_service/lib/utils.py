import pickle


def load_pickle(path: str):
    with open(path, "rb") as f:
        loaded_obj = pickle.load(f)
    return loaded_obj
