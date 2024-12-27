import os
import sys
from pathlib import Path
import logging


log_format="[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"
log_dir="logs"
log_filepath = os.path.join(log_dir, "logfile.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(level=logging.INFO, 
                    format=log_format, 
                    handlers=[logging.FileHandler(log_filepath), 
                              logging.StreamHandler(sys.stdout)])


logger = logging.getLogger('mydatasciencelogger')
