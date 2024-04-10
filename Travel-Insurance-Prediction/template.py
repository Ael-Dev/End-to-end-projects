import os
from pathlib import Path
import logging

# Basic configuration for system logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Name of the project
project_name = "MLProject"

# Folder and file structure
list_of_files = [
    "artifacts/",
    "images/",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    "app.py",
    "requirements.txt",
    "notebooks/Travel-insurance-prediction.ipynb",
]

# Iterate over a list of file paths
for filepath in list_of_files:
    # Convert the file path into a Path object
    filepath = Path(filepath)
    # Split the file path into directory and file name
    filedir, filename = os.path.split(filepath)
    # Check if the directory is not empty
    if filedir != "":
        # Create the directory if it does not exist
        os.makedirs(filedir, exist_ok=True)
        # Log an informative message about the creation of the directory
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    # Check if the file does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Open the file in write mode
        with open(filepath, "w") as f:
            pass  # This is just to create an empty file if it doesn't exist
        # Log an informative message about the creation of the empty file
        logging.info(f"Creating empty file: {filepath}")
    # If the file already exists and is not empty
    else:
        # Log an informative message about the file's existence
        logging.info(f"{filename} already exists")