from config import DATA_DIRPATH
from main import main
from prefect import serve

if __name__ == "__main__":
    train_model_workflow = main.to_deployment(
        name='train_workflow',
        version='0.1.0',
        tags=['train'],
        interval=600,
        parameters={'trainset_path': DATA_DIRPATH},
    )

    serve(train_model_workflow)
