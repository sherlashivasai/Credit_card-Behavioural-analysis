import logging
import os 
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

list_of_files = [
    'src/__init__.py',
    'credit_card.ipynb'

]
# Iterate over the list of files and check if they exist in the current directory

for file in list_of_files:
    file_path = Path(file)
    filedir,filename = os.path.split(file_path)

    if filedir !='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir}')

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f'Creating file: {file_path}')

    else:
        logging.info(f'File already exists: {file_path}')
