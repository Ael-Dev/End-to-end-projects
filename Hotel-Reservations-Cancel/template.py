import os
from pathlib import Path
import logging

# Configuración básica para el registro de logs
log_file = Path() / "logs" / "project.log"
os.makedirs(log_file.parent, exist_ok=True)
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)

# Estructura de carpetas y archivos
list_of_files = [
    "artifacts/artifact",
    "data/data",
    "notebooks/notebook.ipynb",
    "images/",
    "logs/project.log",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/models/__init__.py",
    "src/utils/__init__.py",
    "src/utils/ProjectLogs.py",
    "src/templates/__init__.py",
    "src/templates/index.html",
    "src/static/css/style.css",
    "src/static/js/script.js",
    "app.py",
    "requirements.txt",
]

# Creación de la estructura de carpetas y archivos
for filepath in list_of_files:
    filepath = Path() / filepath
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        if not filepath.is_dir():  # Evitar la creación de archivos vacíos para directorios
            with open(filepath, "w") as f:
                pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

print(f"Estructura de carpetas y archivos para el proyecto -> creada exitosamente.")