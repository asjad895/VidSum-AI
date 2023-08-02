import logging
import os
from datetime import datetime

logdir="logs"
logdir=os.path.join(os.getcwd(),logdir)
os.makedirs(logdir,exist_ok=True)
current_timestamp = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}"

filename=f"log_{current_timestamp}.log"
logfilepath=os.path.join(logdir,filename)

logging.basicConfig(filename=logfilepath,filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)