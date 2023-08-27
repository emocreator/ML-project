import os,sys
import logging
from datetime import datetime

LOG_DIRECTOR ="logs"
LOG_DIRECTOR = os.path.join(os.getcwd(),LOG_DIRECTOR)

os.makedirs(LOG_DIRECTOR,exist_ok=True)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"

log_file_path = os.path.join(LOG_DIRECTOR,file_name)

logging.basicConfig(filename=log_file_path,
                    filemode= "w",
                    format='[%(asctime)s] %(name)s -%(levelname)s -%(message)s',
                    level=logging.INFO
                    )