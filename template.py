import os
import sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

project_name = "datascience"

list_of_files = [
  "github/workflows/.gitkeep",
  f"src/{project_name}/__init__.py",    # __init__.py file is created to have the entrie src folder as a package. any classa nd function can be imported from it.
  f'src/{project_name}/components/__init__.py',
  f'src/{project_name}/utils/__init__.py',
  f'src/{project_name}/utils/common.py',
  f"src/{project_name}/config/__init__.py",
  f"src/{project_name}/config/configuration.py",
  f'src/{project_name}/pipeline/__init__.py',
  f'src/{project_name}/entity/__init__.py',
  f'src/{project_name}/entity/config_entity.py',
  f'src/{project_name}/constants/__init__.py',
  'config/config.yaml',
  'params.yaml',
  'schema.yaml',
  'main.py',
  'setup.py',
  'Dockerfile',
  'research/research.ipynb',
  'app.py'
  
]

for filepath in list_of_files:
  filepath = Path(filepath)
  filedir, filename = os.path.split(filepath)
  
  if filedir != "":
    os.makedirs(filedir, exist_ok=True)   # if file exist, do not make the file
    logging.info(f"Directory created at {filedir} for the file name: {filename}")
    
  if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
    with open(filepath, "w") as file:
      pass
      logging.info(f"File created at {filepath}")
  else: 
    logging.info(f"File already exists at {filepath}")