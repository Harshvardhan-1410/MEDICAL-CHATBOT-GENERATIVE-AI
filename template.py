import os 
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
 
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath) #splitting above filename into directory and filename
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)  # Create directory if it doesn't exist
        logging.info(f"Creating directory: {filedir}")#logging the directory creation
    
    if (not os.path.exists(filepath)) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")  # logging the file creation
    else:
        logging.info(f"{filename} is already exists")