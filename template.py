import os
from pathlib import Path

list_of_files = [
    r".github\workflows\.gitkeep",
    r"src\__init__.py",
    r"src\components\__init__.py",
    r"src\components\data_ingestion.py",
    r"src\components\data_transformation.py",
    r"src\components\model_train.py",
    r"src\components\model_evaluation.py",
    r"src\pipeline\__init__.py",
    r"src\pipeline\training_pipeline.py",
    r"src\pipeline\prediction_pipeline.py",
    r"src\utils\__init__.py",
    r"src\utils\utils.py",
    r"test\unit\__init__.py",
    r"test\integration\__init__.py",
    "init_setup.sh",
    "requirement.txt",
    "requirement_dev.txt",
    "setup.py",
    "setup.cfg",
    r"experiments\experiment.ipynb",
    r"src\logger\logging.py",
    r"src\exception\exception.py",
    "pyproject.toml",
    "tox.ini"

]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
