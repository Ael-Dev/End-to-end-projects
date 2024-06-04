import os
from pathlib import Path
import logging

def configure_logger(project_name):
    """
    Configura el registro de logs para el proyecto.
    
    Args:
        project_name (str): Nombre del proyecto.
    """
    log_file = Path(project_name) / "logs" / "project.log"
    os.makedirs(log_file.parent, exist_ok=True)
    
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='[%(asctime)s]: %(message)s:'
    )
    
    logging.info(f"Logging configured for project: {project_name}")

def get_logger():
    """
    Devuelve el objeto logger configurado.
    
    Returns:
        logging.Logger: Objeto logger configurado.
    """
    return logging.getLogger(__name__)