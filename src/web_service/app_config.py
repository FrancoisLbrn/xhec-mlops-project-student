# MODELS
MODEL_VERSION = "0.0.1"
PATH_TO_PREPROCESSOR = "local_objects/model.pkl"
PATH_TO_MODEL = "local_objects/preprocessor.pkl"
CATEGORICAL_COLS = ['Sex']
NUMERICAL_COLS = [
    'Length',
    'Diameter',
    'Height',
    'Whole_weight',
    'Shucked_weight',
    'Viscera_weight',
    'Shell_weight',
]


# MISC
APP_TITLE = "Abalone MLOPS Project"
APP_DESCRIPTION = (
    "A simple API to predict the age of abalones from physical measurements."
)
APP_VERSION = "0.0.1"
