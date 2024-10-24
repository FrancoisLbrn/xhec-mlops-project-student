# Utils file: add a `load_object` function to load pickle objects

import os
import pickle
from functools import lru_cache

from loguru import logger


@lru_cache
def load_object(filepath: os.PathLike):
    logger.info(f"Loading pickle object from {filepath}")
    with open(filepath, "rb") as f:
        return pickle.load(f)