import pickle
from typing import Any

from prefect import task


@task(name="Save", tags=["Serialize"])
def save_pickle(path: str, obj: Any):
    """Save an object to a pickle file."""

    with open(path, "wb") as f:
        pickle.dump(obj, f)
