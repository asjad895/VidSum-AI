from flask import Flask
from VidSumAI.logger import logging
from VidSumAI.exception import CustomException
import os, sys

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():

    try:
        raise Exception("we are testing our Exception file") # Error
    except Exception as e:
        ML = CustomException(e, sys)
        logging.info(ML.error_message)
        
        logging.info("We are testing our logging file")

        return "WELCOME TO AN INTELLIGENT SYSTEM FORYOU VIDEO UNDERSTANDING"

if __name__ == "__main__":
    app.run(debug = True) # 5000