import logging 
import os
from datetime import datetime

#LOG file name 
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H_%M_%S')}.log"

#LOG file path
LOF_FILE_DIR = os.path.join(os.getcwd(), 'logs')

#Create folder if not available 
os.makedirs(LOG_FILE_DIR, exist_ok=True)

#Log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_PATH)


logging.basicConfig(
    filemode= LOG_FILE_NAME,
    format = '[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s', 
    level= logging.INFO,
)